import requests
import environ
import json
import os

# env variables
environ.Env.read_env()
env = environ.Env()

def get_auth():
    try:
        url = env('APP_URL_AUTH')
        headers = {
            "Content-Type": "application/json"
        } 
        data = {
            "username": env('APP_USERNAME'),
            "access_key": env('APP_ACCESS_KEY')
        }
        resp = requests.post(url, data=json.dumps(data), headers=headers)

        if resp.status_code == requests.codes.ok:
            resp_json = resp.json()
            os.environ['APP_AUTH_TOKEN'] = resp_json['access_token']
        else:
            return None
    except Exception as ex:
        print(ex)
        return None

