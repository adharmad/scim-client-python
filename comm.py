# comm.py
# SCIM request and response

import requests
from config import SERVER_URL
from config import TENANT_NAME
from config import AUTHZ_TOKEN

headers = {
        "X-USER-IDENTITY-DOMAIN-NAME" : TENANT_NAME,
        "Content-Type" : "application/json",
        "Authorization" : AUTHZ_TOKEN
}

def get(obj, ID):
    r = requests.get(SERVER_URL + obj.URI + '/' + ID, headers=headers)
    return r

def post(obj):
    r = requests.post(SERVER_URL + obj.URI, headers=headers, data=obj.to_json())
    return r
