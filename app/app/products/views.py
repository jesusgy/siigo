from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import os
import json
from .classes import Producto

# products 
def products(request,):
    prod = Producto()
    productos = prod.get_products()
    
    return render(request, 'products/products.html', {
        'title': 'Productos',
        'productos': productos
    })

# a product
def product(request, p_id):
    prod = Producto()
    producto = prod.get_product(p_id)
    return render(request, 'products/product.html', {
        'title': 'Producto',
        'producto': producto
    })

# create a product
def create(request,):
    prod = Producto()
    acc_grp = prod.get_accountgroup()
    
    if request.method == 'POST':
        data = {
            "name": request.POST.get('name'),
            "code": request.POST.get('code'),
            "account_group": request.POST.get('account_group'),
            "description": request.POST.get('description'),
        }
        data = json.dumps(data)
        producto = prod.create_product(data)
        return HttpResponseRedirect('/')
    return render(request, 'products/create.html', {
        'title': 'Producto',
        'account_groups': acc_grp,
    })

# modify a product
def edit(request, p_id):
    prod = Producto()
    product = prod.get_product(p_id)
    acc_grp = prod.get_accountgroup()
    if request.method == 'POST':
        data = {
            "name": request.POST.get('name'),
            "code": request.POST.get('code'),
            "account_group": request.POST.get('account_group'),
            "description": request.POST.get('description'),
        }
        data = json.dumps(data)
        producto = prod.update_product(p_id, data)
        return HttpResponseRedirect('/'+p_id+'/get')
    return render(request, 'products/edit.html', {
        'title': 'Producto',
        'producto': product,
        'account_groups': acc_grp,
    })

# delete
def remove(request, p_id):
    prod = Producto()
    producto = prod.remove_product(p_id)
    return HttpResponseRedirect('/')
    