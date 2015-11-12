__author__ = 'ankit.agrawal'

import datetime
import time

from novaclient.client import Client

flavor_id = 42
image_id = "f5d1aefa-5632-4c42-89ef-c115df659875" #Cirros

nova_client = Client('2',
                     username="demo",
                     api_key="demo",
                     auth_url="http://10.69.4.176:5000/v2.0",
                     project_id="demo")

def resize_instance(api_no):
    print "start of api............", api_no
    instance = nova_client.servers.create(name="test_%s"%api_no,
                                          image=image_id,
                                          flavor=flavor_id)
    def _resize_instance():
        instance_obj = nova_client.servers.get(instance)
        instance_status = instance_obj.status
        if instance_status == 'ACTIVE':
            print("Resize instance with flavor m1.tiny")
            nova_client.servers.resize(instance, 1)
            return
        elif instance_status == 'ERROR':
            instance_status = instance_obj.to_dict()['fault']
            print("Instance is in error state %s" %instance_status)
        else:
            time.sleep(2)
            _resize_instance()
    _resize_instance()

    def _delete_instance():
        instance_obj = nova_client.servers.get(instance)
        instance_dict = instance_obj.to_dict()
        task_state = instance_dict['OS-EXT-STS:task_state']
        vm_state = instance_dict['OS-EXT-STS:vm_state']
        if task_state == 'resize_migrated':
            print("deleting instance during resize")
            nova_client.servers.delete(instance)
        elif vm_state == 'resized':
            print("deleting unconfirmed resize instance")
            nova_client.servers.delete(instance)
        else:
            time.sleep(2)
            _delete_instance()
    _delete_instance()

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    duration = 60*240  #in seconds
    test_end_time = time.time() + duration
    total_count = 0
    while 1:
        t = time.time()
        vm_count = len(nova_client.servers.list())
        if t >= test_end_time:
            print("---------end of api calls--------")
            break
        total_count += 1
        try:
            resize_instance(total_count)
        except Exception as e:
            print ("Exit on exception %s " %e)
            break

    print("Total instance delete attempts during resize = %s" % total_count)
