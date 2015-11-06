#! /usr/bin/env python
# users_post.py

import requests, json

url = "http://adc01dyc.us.oracle.com:9246/admin/v1/Users"

headers = {
        "X-USER-IDENTITY-DOMAIN-NAME" : "TENANT1",
        "Content-Type" : "application/json"
}

userPrefix = "idcsUser"
count = 10

def createUser(userName):
    payload = {
        "schemas": [ "urn:ietf:params:scim:schemas:core:2.0:User" ],
        "userName": userName,
        "name": {
            "givenName": userPrefix + "_First",
            "familyName": userPrefix + "_Last"
        },
        "emails": [
            {
                "value": userPrefix + "@example.com",
                "type": "home",
                "primary": True
            }
        ]
    }

    jsonPayload = json.dumps(payload)
    r = requests.post(url, headers=headers, data=jsonPayload)
    print ("Created User " + userName + " response=" + str(r.status_code))

def main():
    for i in range(count):
        userName = userPrefix + str(i)
        createUser(userName)

if __name__ == "__main__":
    main()
