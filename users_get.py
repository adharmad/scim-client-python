#! /usr/bin/env python
# users_post.py

import json
from scim import *
import comm

ID = "10e30a79f6104e15b9df9118d54475a1"

def main():
    r = comm.get(User(), ID)
    u = User.from_json(r.text)
    print ("ID = " + u.id + " username = " + u.userName)
    print ("Fetched User response=" + str(r.status_code))

if __name__ == "__main__":
    main()
