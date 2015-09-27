#!/bin/bash

# variables
user=$1
password=$2
host=$3
# enumerate service catalog
# get keystone scoped token (any)
# for projects
    #how do we enumerate projects
    #try to do nova list for basic read validation

# Project-Scoped Token
curl -i \
  -H "Content-Type: application/json" \
  -d '
{ "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "admin",
          "domain": { "id": "$1" },
          "password": "$2"
        }
      }
    },
    "scope": {
      "project": {
        "name": "demo",
        "domain": { "id": "default" }
      }
    }
  }
}' \
  http://$3:5000/v3/auth/tokens ; echo

/*
#Project-Scoped Token Response:
HTTP/1.1 201 Created
X-Subject-Token: MIIFfQ...
Vary: X-Auth-Token
Content-Type: application/json
Content-Length: 960
Date: Tue, 10 Jun 2014 20:40:14 GMT

{"token": {"methods": ["password"], "roles": [{"id":
 "c703057be878458588961ce9a0ce686b", "name": "admin"}], "expires_at":
 "2014-06-10T21:40:14.360795Z", "project": {"domain": {"id": "default",
 "name": "Default"}, "id": "3d4c2c82bd5948f0bcab0cf3a7c9b48c", "name":
 "demo"}, "catalog": [{"endpoints": [{"url":
 "http://localhost:35357/v2.0", "region": "RegionOne", "interface": "admin",
 "id": "29beb2f1567642eb810b042b6719ea88"}, {"url":
 "http://localhost:5000/v2.0", "region": "RegionOne", "interface":
 "internal", "id": "87057e3735d4415c97ae231b4841eb1c"}, {"url":
 "http://localhost:5000/v2.0", "region": "RegionOne", "interface": "public",
 "id": "ef303187fc8d41668f25199c298396a5"}], "type": "identity", "id":
 "bd7397d2c0e14fb69bae8ff76e112a90", "name": "keystone"}], "extras": {},
 "user": {"domain": {"id": "default", "name": "Default"}, "id":
 "3ec3164f750146be97f21559ee4d9c51", "name": "admin"}, "issued_at":
 "2014-06-10T20:40:14.360822Z"}}
*/


# Domain-Scoped Token (requires role assignment on domain first, allegedly):
curl -i \
  -H "Content-Type: application/json" \
  -d '
{ "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "admin",
          "domain": { "id": "default" },
          "password": "adminpwd"
        }
      }
    },
    "scope": {
      "domain": {
        "id": "default"
      }
    }
  }
}' \
  http://localhost:5000/v3/auth/tokens ; echo

#Domain-Scoped Token Response:
HTTP/1.1 201 Created
X-Subject-Token: MIIFNg...
Vary: X-Auth-Token
Content-Type: application/json
Content-Length: 889
Date: Tue, 10 Jun 2014 20:52:59 GMT

{"token": {"domain": {"id": "default", "name": "Default"}, "methods":
["password"], "roles": [{"id": "c703057be878458588961ce9a0ce686b", "name":
"admin"}], "expires_at": "2014-06-10T21:52:58.852167Z", "catalog":
[{"endpoints": [{"url": "http://localhost:35357/v2.0", "region": "RegionOne",
"interface": "admin", "id": "29beb2f1567642eb810b042b6719ea88"}, {"url":
"http://localhost:5000/v2.0", "region": "RegionOne", "interface": "internal",
"id": "87057e3735d4415c97ae231b4841eb1c"}, {"url":
"http://localhost:5000/v2.0", "region": "RegionOne", "interface": "public",
"id": "ef303187fc8d41668f25199c298396a5"}], "type": "identity", "id":
"bd7397d2c0e14fb69bae8ff76e112a90", "name": "keystone"}], "extras": {},
"user": {"domain": {"id": "default", "name": "Default"}, "id":
"3ec3164f750146be97f21559ee4d9c51", "name": "admin"}, "issued_at":
"2014-06-10T20:52:58.852194Z"}}



# Python (3?) methods for getting scoped tokens using 1) urllib and 2) requests:
from __future__ import print_function

import urllib2
import json


if __name__ == "__main__":
    json_payload = {
        "auth": {
            "tenantName": "demo",
            "passwordCredentials": {
                "username": "demo",
                "password": "password"
            }
        }
    }

    headers = {'content-type': 'application/json', 'accept': 'application/json'}

    request = urllib2.Request(url='http://localhost:5000/v2.0/tokens',
                              data=json.dumps(json_payload),
                              headers=headers)

    keystone_response = urllib2.urlopen(request)

    returned_data = json.loads(keystone_response.read())

    if keystone_response.getcode() == 200:
        print(returned_data)
    else:
        print('Something went wrong!')
The final way I’ll show will be using the Requests library for Python.

from __future__ import print_function

import requests
import json


if __name__ == "__main__":
    json_payload = {
        "auth": {
            "tenantName": "demo",
            "passwordCredentials": {
                "username": "demo",
                "password": "password"
            }
        }
    }

    headers = {'content-type': 'application/json', 'accept': 'application/json'}

    response = requests.post(url='http://localhost:5000/v2.0/tokens',
                             data=json.dumps(json_payload),
                             headers=headers)

    if response.status_code == requests.codes.ok:
        print(response.json())
    else:
        print('Something went wrong!')
