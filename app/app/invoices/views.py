from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import os
import json
from .classes import Invoice

# invoices 
def invoices(request,):
    invoice = Invoice()
    invoices = invoice.get_invoices()
    
    return render(request, 'invoices/invoices.html', {
        'title': 'Facturas',
        'invoices': invoices
    })

# a invoice
def invoice(request, i_id):
    invoice = Invoice()
    invoice = invoice.get_invoice(i_id)
    return render(request, 'invoices/invoice.html', {
        'title': 'Factura',
        'invoice': invoice
    })