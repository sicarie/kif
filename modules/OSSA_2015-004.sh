1. Create image using task api

$ curl -i -X POST -H 'User-Agent: python-glanceclient' -H 'Content-Type: application/json' -H 'Accept-Encoding: gzip, deflate, compress' -H 'Accept: */*' -H 'X-Auth-Token: 35a9e49237b74eddbe5057eb434b3f9e' -d '{"type": "import", "input": {"import_from": "http://releases.ubuntu.com/14.10/ubuntu-14.10-server-i386.iso", "import_from_format": "raw", "image_properties": {"disk_format": "raw", "container_format": "bare", "name": "task_image"}}}' http://10.69.4.176:9292/v2/tasks

2. wait until image becomes active.
3. Confirm image is in active state.
   $ glance image-list
4. Delete the image
   $ glance image-delete <image-id>
5. Verify image-list does not show deleted image
   $ glance image-list
