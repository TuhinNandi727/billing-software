from django import forms
from .models import Product, Customer, Invoice
 
class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = '__all__'

class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = '__all__'

class InvoiceForm(forms.ModelForm):
  class Meta:
    model = Invoice
    fields = ['customer']