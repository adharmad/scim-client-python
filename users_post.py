#! /usr/bin/env python
# users_post.py

import requests, json

url = "http://adc01dyc.us.oracle.com:9246/admin/v1/Users"

headers = {
        "X-USER-IDENTITY-DOMAIN-NAME" : "TENANT1",
        "Content-Type" : "application/json"
}

userPrefix = "idcsUser"

def main():
    payload = {
        "schemas": [ "urn:ietf:params:scim:schemas:core:2.0:User" ],
        "userName": userPrefix,
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
    #print (r.json())
    print ("Created User " + userPrefix + " response=" + str(r.status_code))

if __name__ == "__main__":
    main()
