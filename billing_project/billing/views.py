from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import date
from .models import Product, Customer, Invoice, InvoiceItem
from .forms import ProductForm, CustomerForm, InvoiceForm


# for dashboard
def dashboard(request):
  return render(request, 'dashboard.html')


# for Product
def product_list(request):
  products = Product.objects.all()
  return render(request, 'product/product_list.html', {'products': products})

def add_product(request):
  form = ProductForm()

  if request.method == 'POST':
    form = ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(product_list)

  return render(request, 'product/add_product.html', {'form': form})

def edit_product(request, id):
  product = Product.objects.get(id=id)
  form = ProductForm(instance=product)

  if request.method=='POST':
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
      form.save()
      return redirect('product_list')
  return render(request, 'product/edit_product.html', {'form':form})

def delete_product(request, id):
  product = Product.objects.get(id=id)
  product.delete()
  return redirect('product_list')


# for Customer
def customer_list(request):
  customers = Customer.objects.all()
  return render(request, 'customer/customer_list.html', {'customers': customers})

def add_customer(request):
  form = CustomerForm()

  if request.method == 'POST':
    form = CustomerForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(customer_list)

  return render(request, 'customer/add_customer.html', {'form': form})

def edit_customer(request, id):
  customer = Customer.objects.get(id=id)
  form = CustomerForm(instance=customer)

  if request.method=='POST':
    form = CustomerForm(request.POST, instance=customer)
    if form.is_valid():
      form.save()
      return redirect('customer_list')
  return render(request, 'customer/edit_customer.html', {'form':form})

def delete_customer(request, id):
  customer = Customer.objects.get(id=id)
  customer.delete()
  return redirect('customer_list')


# for invoice
def create_invoice(request):
    form = InvoiceForm()
    products = Product.objects.all()

    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.total_amount = 0
            invoice.save()

            total_amount = 0
            for product in products:
                qty = request.POST.get(f'quantity_{product.id}')
                if qty and int(qty) > 0:
                    quantity = int(qty)
                    price = product.price
                    total = quantity * price
                    InvoiceItem.objects.create(
                        invoice=invoice,
                        product=product,
                        quantity=quantity,
                        price=price,
                        total=total
                    )
                    product.quantity -= quantity
                    product.save()
                    total_amount += total

            # GST calculation
            subtotal = total_amount
            gst = float(subtotal) * 0.18
            grand_total = float(subtotal) + gst

            invoice.subtotal = subtotal
            invoice.gst = gst
            invoice.total_amount = grand_total
            invoice.save()

            return redirect('invoice_detail', id=invoice.id)

    return render(request, 'create_bill/create_invoice.html', {
        'form': form,
        'products': products
    })


# for invoice detail
def invoice_detail(request, id):
  invoice = Invoice.objects.get(id=id)
  items = InvoiceItem.objects.filter(invoice=invoice)
  return render(request, 'create_bill/invoice_detail.html', {'invoice': invoice, 'items': items})


# for low stock alert
def dashboard(request):
  low_stock = Product.objects.filter(quantity__lt=5)
  return render(request, 'dashboard.html', {'low_stock' : low_stock})


# for sales report view
def sales_report(request):
  invoices = Invoice.objects.all()
  total_sales = Invoice.objects.aggregate(total=Sum('total_amount'))['total']

  today = date.today()
  today_sales = Invoice.objects.filter(date__date=today).aggregate(total=Sum('total_amount'))['total']

  if total_sales is None:
    total_sales = 0

  if today_sales is None:
    today_sales = 0

  return render(request, 'reports/sales_report.html',{'invoices' : invoices,'total_sales' : total_sales,'today_sales' : today_sales})