import requests
import os
from app.auth import get_auth

class Producto:
    def __init__(self,):
        self.AUTH_TOKEN = os.environ.get('APP_AUTH_TOKEN')

        self.URL_BASE = os.environ.get('APP_URL_BASE')
        self.URL_LIST_PROD = self.URL_BASE + 'products?'
        self.URL_CREATE_PROD = self.URL_BASE + 'products'
        self.URL_UPDATE_PROD = self.URL_BASE + 'products/'
        self.URL_ONE_PROD = self.URL_BASE + 'products/'
        self.URL_ACCOUNT_GROUP = self.URL_BASE + 'account-groups'
        self.URL_TAXES = self.URL_BASE + 'taxes'

        self.HEADERS = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+self.AUTH_TOKEN
        }

    # lista de productos
    def get_products(self, filters=None, ):
        resp = requests.get(self.URL_LIST_PROD, data=filters, headers=self.HEADERS)
        
        if resp.status_code == 200:
            return resp.json()
        return None

    # un producto
    def get_product(self, p_id):
        resp = requests.get(self.URL_ONE_PROD+p_id, data={}, headers=self.HEADERS)

        if resp.status_code == 200:
            return resp.json()
        return None

    # del producto
    def remove_product(self, p_id):
        resp = requests.delete(self.URL_ONE_PROD+p_id, data={}, headers=self.HEADERS)

        if resp.status_code == 200:
            return resp.json()
        return None
  
    # add producto
    def create_product(self, data):
        resp = requests.post(self.URL_CREATE_PROD, data=data, headers=self.HEADERS)

        if resp.status_code == 201:
            return resp.json()
        return None
  
    # update producto
    def update_product(self, p_id, data):
        resp = requests.put(self.URL_UPDATE_PROD+p_id, data=data, headers=self.HEADERS)

        if resp.status_code == 200:
            return resp.json()
        return None

    # acc group
    def get_accountgroup(self,):
        resp = requests.get(self.URL_ACCOUNT_GROUP, headers=self.HEADERS)

        if resp.status_code == 200:
            return resp.json()
        return None

    # taxes
    def get_taxes(self,):
        resp = requests.get(self.URL_TAXES, headers=self.HEADERS)

        if resp.status_code == 200:
            return resp.json()
        return None
