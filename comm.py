# comm.py
# SCIM request and response

import requests
from config import SERVER_URL
from config import TENANT_NAME

headers = {
        "X-USER-IDENTITY-DOMAIN-NAME" : TENANT_NAME,
        "Content-Type" : "application/json"
}

def post(obj):
    r = requests.post(SERVER_URL + obj.URI, headers=headers, data=obj.to_json())
    return r
