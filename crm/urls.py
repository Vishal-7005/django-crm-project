from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customers/', views.customers, name='customers'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('update-customer/<int:pk>/', views.update_customer, name='update_customer'),
    path('delete-customer/<int:pk>/', views.delete_customer, name='delete_customer'),
]