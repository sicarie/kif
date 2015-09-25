#!/bin/bash

# Get the revocation list:

curl -s -H "X-Auth-Token: $OS_TOKEN" \
  http://localhost:35357/v2.0/tokens/revoked |
 jq -r .signed |
 openssl cms -verify \
  -certfile /etc/keystone/ssl/certs/signing_cert.pem \
  -CAfile /etc/keystone/ssl/certs/ca.pem \
  -inform PEM \
  -nosmimecap -nodetach -nocerts -noattr 2>/dev/null |
 python -m json.tool


# Example response:
#{
#    "revoked": [
#        {
#            "expires": "2014-06-10T21:40:14Z",
#            "id": "e6e2b5c9092751f88d2bcd30b09777a9"
#        },
#        {
#            "expires": "2014-06-10T21:47:29Z",
#            "id": "883ef5d610bd1c68fbaa8ac528aa9f17"
#        },
#        {
#            "expires": "2014-06-10T21:51:52Z",
#            "id": "41775ff4838f8f406b7bad28bea0dde6"
#        }
#    ]
#}
