from django.http import HttpResponseRedirect
from django.shortcuts import render
import os
from .classes import Producto

# products 
def products(request,):
    prod = Producto()
    productos = prod.get_products()
    '''
    {
        'pagination': {'page': 1, 'page_size': 25, 'total_results': 3}, 
        'results': [
            {'id': 'a1407123-518a-44a3-a07e-5bf54831f021', 'code': '4435', 
                'name': 'Producto prueba API V344', 
                'account_group': {'id': 395}, 
                'type': 'Product', 'stock_control': False, 'active': True, 'tax_classification': 'Excluded', 
                'tax_included': False, 'tax_consumption_value': 0.0, 
                'taxes': [], 
                'prices': [
                    {
                        'currency_code': 'COP', 
                    'price_list': [
                        {'position': 2377, 'name': 'Precio de venta 1', 'value': 12500.0}
                        ]
                    }
                ], 
                'unit_label': ' ', 'reference': ' ', 'description': ' ', 
                'additional_fields': {'barcode': '', 'brand': '', 'tariff': '', 'model': ''}, 
                'available_quantity': 0.0, 'warehouses': [], 
                'metadata': {'created': '2021-02-26T19:58:30.109Z'}
            }, 
            {'id': '1cf69d96-b35a-4f80-8f13-c0c5804a5054', 'code': 'Sku-4', 
                'name': 'Camiseta de algodón', 
                'account_group': {'id': 395}, 
                'type': 'Product', 'stock_control': False, 'active': True, 'tax_classification': 'Exempt', 
                'tax_included': False, 'tax_consumption_value': 0.0, 
                'taxes': [], 
                'prices': [
                    {
                        'currency_code': 'COP', 
                        'price_list': [
                            {'position': 2377, 'name': 'Precio de venta 1', 'value': 12000.0}
                        ]
                    }
                ], 
                'unit_label': 'unidad', 'reference': 'REF1', 'description': 'Camiseta de algodón blanca', 
                'additional_fields': {'barcode': 'B0123', 'brand': 'Gef', 'tariff': '151612', 'model': 'Loiry'}, 
                'available_quantity': 0.0, 'warehouses': [], 
                'metadata': {'created': '2021-02-26T18:17:43.008Z', 'last_updated': '2021-02-26T18:20:51.321Z'}
            }, 
            {'id': 'b801cda3-b36b-4a44-bdc3-49d4dcf5fa39', 'code': 'Sku-3', 
                'name': 'Producto de prueba', 'account_group': {'id': 395}, 
                'type': 'Product', 'stock_control': False, 'active': True, 'tax_classification': 'Taxed', 
                'tax_included': False, 'tax_consumption_value': 0.0, 
                'taxes': [], 
                'prices': [
                    {
                        'currency_code': 'COP', 
                        'price_list': []
                    }
                ], 'description': '', 
                'additional_fields': {}, 
                'available_quantity': 0.0, 'warehouses': [], 
                'metadata': {'created': '2021-02-26T18:17:22.013Z'}
            }
        ], 
        '_links': {
            'self': {
                'href': 'https://api.siigo.com/v1/products?page=1&page_size=25'
            }
            'previous': {
                'href': 'https://api.siigo.com/v1/products?page=1&page_size=25'
            }
            'next': {
                'href': 'https://api.siigo.com/v1/products?page=1&page_size=25'
            }
        }
    }
    '''
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
    if request.method == 'POST':
        producto = prod.create_product(data)
    return render(request, 'products/create.html', {
        'title': 'Producto',
    })

# modify a product
def edit(request, id):
    pass

# delete
def remove(request, p_id):
    prod = Producto()
    producto = prod.remove_product(p_id)
    return HttpResponseRedirect('/')
    