from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
    path('', views.clients, name='all'),
    path('<str:c_id>/get', views.client, name='client_one'),
]