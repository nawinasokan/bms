from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('add/', views.customer_create, name='customer_add'),
    path('edit/<int:pk>/', views.customer_update, name='customer_edit'),
    path('delete/<int:pk>/', views.customer_delete, name='customer_delete'),
]
