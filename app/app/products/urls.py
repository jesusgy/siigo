from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products, name='all'),
    path('create', views.create, name='product_create'),
    path('<str:p_id>/get', views.product, name='product_one'),
    path('<str:p_id>/edit', views.edit, name='product_edit'),
    path('<str:p_id>/remove', views.remove, name='product_remove'),
]