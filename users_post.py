#! /usr/bin/env python
# users_post.py

import json
from scim import *
import comm

userPrefix = "testUser25"

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

    r = comm.post(user)
    u = User.from_json(r.text)
    print ("ID = " + u.id + " username = " + u.userName)
    print ("Created User " + userPrefix + " response=" + str(r.status_code))

if __name__ == "__main__":
    main()
