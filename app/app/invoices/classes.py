import requests
import os
from app.auth import get_auth

class Invoice:
    def __init__(self,):
        self.AUTH_TOKEN = os.environ.get('APP_AUTH_TOKEN')

        self.URL_BASE = os.environ.get('APP_URL_BASE')
        self.URL_LIST_INVOICES = self.URL_BASE + 'invoices?'
        self.URL_ONE_INVOICE = self.URL_BASE + 'invoices/'

        self.HEADERS = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+self.AUTH_TOKEN
        }

    # clients
    def get_invoices(self, filters=None, ):
        resp = requests.get(self.URL_LIST_INVOICES, data=filters, headers=self.HEADERS)
        
        if resp.status_code == 200:
            return resp.json()
        return None

    # client
    def get_invoice(self, i_id):
        resp = requests.get(self.URL_ONE_INVOICE+i_id, data={}, headers=self.HEADERS)

        if resp.status_code == 200:
            return resp.json()
        return None