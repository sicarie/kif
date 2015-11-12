Steps to reproduce:
- create volume and attach to vm,
- create a qcow2 signature with base-file[1] from within the vm and
- trigger upload to glance with "cinder upload-to-image --disk-type qcow2"[2].
The image uploaded to glance will have /etc/passwd from the cinder-volume host embedded.
Affected versions: tested on 2014.1.3, found while reading 2014.2.1
