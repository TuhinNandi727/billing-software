from django.contrib import admin

# Register your models here.
from .models import Product, Customer,Invoice,InvoiceItem

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)