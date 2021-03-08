import requests
import os
from app.auth import get_auth

class Client:
    def __init__(self,):
        self.AUTH_TOKEN = os.environ.get('APP_AUTH_TOKEN')

        self.URL_BASE = os.environ.get('APP_URL_BASE')
        self.URL_LIST_CLIENTS = self.URL_BASE + 'customers?'
        self.URL_ONE_CLIENT = self.URL_BASE + 'customers/'

        self.HEADERS = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+self.AUTH_TOKEN
        }

    # clients
    def get_clients(self, filters=None, ):
        resp = requests.get(self.URL_LIST_CLIENTS, data=filters, headers=self.HEADERS)
        
        if resp.status_code == 200:
            return resp.json()
        return None

    # client
    def get_client(self, c_id):
        resp = requests.get(self.URL_ONE_CLIENT+c_id, data={}, headers=self.HEADERS)

        if resp.status_code == 200:
            return resp.json()
        return None