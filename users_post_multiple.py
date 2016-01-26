#! /usr/bin/env python
# users_post_multiple.py

import json
from scim import *
import comm

userPrefix = "helloUser"
count = 10

def createUser(userName):
    user = User()
    user.userName = userName
    user.name = { 
        "givenName" : userName + "_First",
        "familyName" : userName + "_Last",
    }
    email1 = {
        "value" : userName + "@example.com",
        "type" : "home",
        "primary" : True
    }
    user.emails =[email1]

    r = comm.post(user)
    u = User.from_json(r.text)
    print ("ID = " + u.id + " username = " + u.userName)
    print ("Created User " + userPrefix + " response=" + str(r.status_code))

def main():
    for i in range(count):
        userName = userPrefix + str(i)
        createUser(userName)

if __name__ == "__main__":
    main()
