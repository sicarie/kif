__author__ = 'pranali.deore'

from glanceclient import Client

import datetime
import time
import uuid

total_images_created = 0
deleted_in_saving_state = 0
total_images_deleted = 0

OS_AUTH_TOKEN = "ea86ffcc04484b9d8e963911040b2d9a"
OS_IMAGE_ENDPOINT = "http://192.168.0.2:9292/v2"
file_location = open('cool_file', 'r')

glance = Client('2', endpoint=OS_IMAGE_ENDPOINT, token=OS_AUTH_TOKEN)


def create_delete_image():
    id = str(uuid.uuid4())
    image = glance.images.create(name=id,
                                 disk_format='ami',
                                 container_format='bare')
    glance.images.upload(image.id, file_location)
    global total_images_created, deleted_in_saving_state, total_images_deleted
    total_images_created += 1
    print("Image status = = %s" % image.status)

    #Initially image goes into queued state hence added sleep here
    time.sleep(3)

    image = glance.images.get(image.id)
    if image.status == "saving":
        print("Image status = = %s" % image.status)
        glance.images.delete(image)
        print("Image %s deleted in saving state" % image.id)
        deleted_in_saving_state += 1
    else:
        # if image status is set to active after 3 sec of sleep
        # delete the image
        glance.images.delete(image.id)

    #number of total deleted images
    total_images_deleted += 1



if __name__ == '__main__':
    start_time = datetime.datetime.now()
    duration = 600 #in seconds
    stop_time = time.mktime(start_time.timetuple()) + duration

    while 1:
        create_delete_image()
        t = time.time()
        if t >= stop_time:
            break

    print 'Total images created', total_images_created
    print 'Images deleted in saving state ', deleted_in_saving_state
    print 'Total images deleted ', total_images_deleted
