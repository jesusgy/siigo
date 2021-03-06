from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products, name='products'),
    path('create/', views.create, name='product_create'),
    path('<str:p_id>/', views.product, name='product_one'),
    path('<str:p_id>/remove/', views.remove, name='product_remove'),
]