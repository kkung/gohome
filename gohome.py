#-*- encoding: utf-8 -*-

import json, urllib2, socket, re, sys
from contextlib import closing

import re
__RE_RESULT__ = re.compile("<b>([^<]*)</b>", re.I | re.S | re.M)

socket.setdefaulttimeout(120)

data = json.load(open(sys.argv[1]))
dr = data['request']
req = urllib2.Request(dr['url'])

for h in dr['headers']:
	req.add_header(h['name'],  h['value'])

req.data = dr['postData']['text']

fp = urllib2.urlopen(req, )
with closing(fp):
	result = fp.read().decode('cp949')

print 
for m in __RE_RESULT__.findall(result):
	if len(m.strip()) > 0:
		print u'[%s] %s' % (sys.argv[1], m)