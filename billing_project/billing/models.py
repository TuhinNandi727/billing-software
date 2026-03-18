from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=50)
  code = models.CharField(max_length=10)
  category = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity = models.IntegerField()
  # tax = models.DecimalField(max_digits=5, decimal_places=2)

  # is used to define how an object of the model will appear as text.
  def __str__(self): # self is current product object
    return f"{self.name} ({self.code})"


class Customer(models.Model):
  name = models.CharField(max_length=50)
  phone = models.CharField(max_length=15)
  email = models.EmailField()
  address = models.TextField()
  def __str__(self): 
    return self.name
  

class Invoice(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)
  subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  gst = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  total_amount = models.DecimalField(max_digits=10,decimal_places=2)
  def __str__(self): 
    return f"Invoice {self.id}"
  
class InvoiceItem(models.Model):
  invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits=10,decimal_places=2)
  total = models.DecimalField(max_digits=10,decimal_places=2)
  
