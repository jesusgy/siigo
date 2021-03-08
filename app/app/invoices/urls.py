from django.urls import path
from . import views

app_name = 'invoices'
urlpatterns = [
    path('', views.invoices, name='all'),
    path('<str:i_id>/get', views.invoice, name='invoice_one'),
]