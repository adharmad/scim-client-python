#! /usr/bin/env python
# users_post.py

import requests, json
from config import SERVER_URL
from config import TENANT_NAME
from scim import *

headers = {
        "X-USER-IDENTITY-DOMAIN-NAME" : TENANT_NAME,
        "Content-Type" : "application/json"
}

userPrefix = "testUser24"

def main():
    user = User()
    user.userName = userPrefix
    user.name = { 
        "givenName" : userPrefix + "_First",
        "familyName" : userPrefix + "_Last",
    }
    email1 = {
        "value" : userPrefix + "@example.com",
        "type" : "home",
        "primary" : True
    }
    user.emails =[email1]

    r = requests.post(SERVER_URL, headers=headers, data=user.to_json())
    u = User.from_json(r.text)
    print ("ID = " + u.id + " username = " + u.userName)
    print ("Created User " + userPrefix + " response=" + str(r.status_code))

if __name__ == "__main__":
    main()
