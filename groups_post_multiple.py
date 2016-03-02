#! /usr/bin/env python
# groups_post_multiple.py

import json
from scim import *
import comm

groupPrefix = "fooGrp"
count = 10

def createGroup(groupName):
    group = Group()
    group.displayName = groupName

    r = comm.post(group)
    g = Group.from_json(r.text)
    print ("ID = " + g.id + " displayName = " + g.displayName)
    print ("Created Group " + groupPrefix + " response=" + str(r.status_code))

def main():
    for i in range(count):
        groupName = groupPrefix + str(i)
        createGroup(groupName)

if __name__ == "__main__":
    main()
