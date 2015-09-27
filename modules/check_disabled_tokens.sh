#!/bin/bash

# Input: 1 - a token; 2 - an endpoint
# Desc: Disabling a tenant does not necessarily disable corresponding
#       keystone tokens
# Ref: OSSN-32
# Affects: Keystone, Folsom, Grizzly


token=$1
endpoint=$2
curl -H "$X-Auth-Token:$token" http://$endpoint:35357/v2.0/tenants

#Returns:
#
#{
#    "tenants_links": [],
#    "tenants": [
#        {
#            "enabled": false,
#            "description": "None",
#            "name": "project-y",
#            "id": "3"
#        },
#        {
#            "enabled": true,
#            "description": "None",
#            "name": "ANOTHER:TENANT",
#            "id": "2"
#        },
#        {
#            "enabled": true,
#            "description": "None",
#            "name": "customer-x",
#            "id": "1"
#        }
#    ]
#}
