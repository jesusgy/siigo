from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import os
import json
from .classes import Client

# clients 
def clients(request,):
    client = Client()
    clients = client.get_clients()
    
    return render(request, 'clients/clients.html', {
        'title': 'Clientes',
        'clients': clients
    })

# a client
def client(request, c_id):
    client = Client()
    client = client.get_client(c_id)
    return render(request, 'clients/client.html', {
        'title': 'Cliente',
        'client': client
    })