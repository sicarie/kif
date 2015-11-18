$ glance image-create --name test1 --disk-format raw --container-format bare --file /etc/fstab
+------------------+--------------------------------------+
| Property         | Value                                |
+------------------+--------------------------------------+
| checksum         | 9cb02fe7fcac26f8a25d6db3109063ae     |
| container_format | bare                                 |
| created_at       | 2015-08-07T11:41:21.000000           |
| deleted          | False                                |
| deleted_at       | None                                 |
| disk_format      | raw                                  |
| id               | cc658de9-039a-46d7-829a-dc1f08cac153 |
| is_public        | False                                |
| min_disk         | 0                                    |
| min_ram          | 0                                    |
| name             | test1                                |
| owner            | 411423405e10431fb9c47ac5b2446557     |
| protected        | False                                |
| size             | 145                                  |
| status           | active                               |
| updated_at       | 2015-08-07T11:41:22.000000           |
| virtual_size     | None                                 |
+------------------+--------------------------------------+

$ curl -X PUT http://127.0.0.1:9292/v1/images/cc658de9-039a-46d7-829a-dc1f08cac153 -H 'X-Auth-Token: 6e46dc0e098042bfa1ebe8359578e13f' -H 'x-image-meta-status: queued' | python -mjson.tool
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   485  100   485    0     0   2928      0 --:--:-- --:--:-- --:--:--  2957
{
    "image": {
        "checksum": "9cb02fe7fcac26f8a25d6db3109063ae",
        "container_format": "bare",
        "created_at": "2015-08-07T11:41:21.000000",
        "deleted": false,
        "deleted_at": null,
        "disk_format": "raw",
        "id": "cc658de9-039a-46d7-829a-dc1f08cac153",
        "is_public": false,
        "min_disk": 0,
        "min_ram": 0,
        "name": "test1",
        "owner": "411423405e10431fb9c47ac5b2446557",
        "properties": {},
        "protected": false,
        "size": 145,
        "status": "queued",
        "updated_at": "2015-08-07T11:41:54.000000",
        "virtual_size": null
    }
}



$ glance --os-image-api-version 2 image-upload  cc658de9-039a-46d7-829a-dc1f08cac153  < /tmp/hi


$ glance image-show cc658de9-039a-46d7-829a-dc1f08cac153
+------------------+--------------------------------------+
| Property         | Value                                |
+------------------+--------------------------------------+
| checksum         | 764efa883dda1e11db47671c4a3bbd9e     |
| container_format | bare                                 |
| created_at       | 2015-08-07T11:41:21.000000           |
| deleted          | False                                |
| disk_format      | raw                                  |
| id               | cc658de9-039a-46d7-829a-dc1f08cac153 |
| is_public        | False                                |
| min_disk         | 0                                    |
| min_ram          | 0                                    |
| name             | test1                                |
| owner            | 411423405e10431fb9c47ac5b2446557     |
| protected        | False                                |
| size             | 3                                    |
| status           | active                               |
| updated_at       | 2015-08-07T11:42:25.000000           |
+------------------+--------------------------------------+


$ glance image-download cc658de9-039a-46d7-829a-dc1f08cac153  | cat
hi

######################################################

$ glance image-create --name test1 --disk-format raw --container-format bare
+------------------+--------------------------------------+
| Property         | Value                                |
+------------------+--------------------------------------+
| checksum         | None                                 |
| container_format | bare                                 |
| created_at       | 2015-08-07T10:30:42.000000           |
| deleted          | False                                |
| deleted_at       | None                                 |
| disk_format      | raw                                  |
| id               | 38a476ad-fce7-4252-9848-db44ecae7757 |
| is_public        | False                                |
| min_disk         | 0                                    |
| min_ram          | 0                                    |
| name             | test1                                |
| owner            | 411423405e10431fb9c47ac5b2446557     |
| protected        | False                                |
| size             | 0                                    |
| status           | queued                               |
| updated_at       | 2015-08-07T10:30:42.000000           |
| virtual_size     | None                                 |
+------------------+--------------------------------------+

$ glance image-update --location 'swift+http://demo%3Ademo:<password>@10.0.0.85:5000/v2.0/container1/HACKING.rst' 38a476ad-fce7-4252-9848-db44ecae7757 | python -m json.tool
No JSON object could be decoded

$ glance image-show 38a476ad-fce7-4252-9848-db44ecae7757
+------------------+--------------------------------------+
| Property         | Value                                |
+------------------+--------------------------------------+
| container_format | bare                                 |
| created_at       | 2015-08-07T10:30:42.000000           |
| deleted          | False                                |
| disk_format      | raw                                  |
| id               | 38a476ad-fce7-4252-9848-db44ecae7757 |
| is_public        | False                                |
| min_disk         | 0                                    |
| min_ram          | 0                                    |
| name             | test1                                |
| owner            | 411423405e10431fb9c47ac5b2446557     |
| protected        | False                                |
| size             | 239                                  |
| status           | active                               |
| updated_at       | 2015-08-07T10:31:07.000000           |
+------------------+--------------------------------------+

$ curl -X PUT http://127.0.0.1:9292/v1/images/38a476ad-fce7-4252-9848-db44ecae7757  -H 'X-Auth-Token: 651a0607bcf54ad69706a500bbac3db7' -H 'x-image-meta-status: queued' | python -mjson.tool
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   455  100   455    0     0   1514      0 --:--:-- --:--:-- --:--:--  1521
{
    "image": {
        "checksum": null,
        "container_format": "bare",
        "created_at": "2015-08-07T10:30:42.000000",
        "deleted": false,
        "deleted_at": null,
        "disk_format": "raw",
        "id": "38a476ad-fce7-4252-9848-db44ecae7757",
        "is_public": false,
        "min_disk": 0,
        "min_ram": 0,
        "name": "test1",
        "owner": "411423405e10431fb9c47ac5b2446557",
        "properties": {},
        "protected": false,
        "size": 239,
        "status": "queued",
        "updated_at": "2015-08-07T10:32:07.000000",
        "virtual_size": null
    }
}

$ glance image-update --location 'swift+http://demo%3Ademo:<password>@10.0.0.85:5000/v2.0/container1/README.rst' 38a476ad-fce7-4252-9848-db44ecae7757 | python -m json.tool
No JSON object could be decoded

$ glance image-show 38a476ad-fce7-4252-9848-db44ecae7757
+------------------+--------------------------------------+
| Property         | Value                                |
+------------------+--------------------------------------+
| container_format | bare                                 |
| created_at       | 2015-08-07T10:30:42.000000           |
| deleted          | False                                |
| disk_format      | raw                                  |
| id               | 38a476ad-fce7-4252-9848-db44ecae7757 |
| is_public        | False                                |
| min_disk         | 0                                    |
| min_ram          | 0                                    |
| name             | test1                                |
| owner            | 411423405e10431fb9c47ac5b2446557     |
| protected        | False                                |
| size             | 933                                  |
| status           | active                               |
| updated_at       | 2015-08-07T10:32:36.000000           |
+------------------+--------------------------------------+


$ glance image-download 38a476ad-fce7-4252-9848-db44ecae7757 | cat | head
Python bindings to the OpenStack Images API
=============================================

This is a client library for Glance built on the OpenStack Images API. It provides a Python API (the ``glanceclient`` module) and a command-line tool (``glance``). This library fully supports the v1 Images API, while support for the v2 API is in progress.

Development takes place via the usual OpenStack processes as outlined in the `developer guide <http://docs.openstack.org/infra/manual/developers.html>`_.  The master repository is in `Git <https://git.openstack.org/cgit/openstack/python-glanceclient>`_.

See release notes and more at `<http://docs.openstack.org/developer/python-glanceclient/>`_.

* License: Apache License, Version 2.
