from django.urls import path
from . import views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),

  path('products/', views.product_list, name='product_list'),
  path('add-product/', views.add_product, name='add_product'),
  path('edit-product/<int:id>/', views.edit_product, name='edit_product'),
  path('delete-product/<int:id>/', views.delete_product, name='delete_product'),

  path('customers/', views.customer_list, name='customer_list'),
  path('add-customer/', views.add_customer, name='add_customer'),
  path('edit-customer/<int:id>/', views.edit_customer, name='edit_customer'),
  path('delete-customer/<int:id>/', views.delete_customer, name='delete_customer'),

  path('create-invoice/', views.create_invoice, name='create_invoice'),
  path('invoice/<int:id>/', views.invoice_detail, name='invoice_detail'),

  path('reports/', views.sales_report, name='sales_report'),
]