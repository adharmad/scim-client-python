#! /usr/bin/env python
# groups_post.py

import json
from scim import *
import comm

grpPrefix = "testGroup4"

def main():
    group = Group()
    group.displayName = grpPrefix

    r = comm.post(group)
    g = Group.from_json(r.text)
    print ("ID = " + g.id + " displayName = " + g.displayName)
    print ("Created Group " + grpPrefix + " response=" + str(r.status_code))

if __name__ == "__main__":
    main()
