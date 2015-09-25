#!/bin/bash

for i in {1..100}
do
  curl -b "sessionid=aaaaa;" http://HORIZON__IP/auth/login/ &> /dev/null
done
