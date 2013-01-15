#-*- encoding: utf-8 -*-
import gevent
from gevent import monkey; monkey.patch_all()
import json, urllib2, socket, re, sys
from contextlib import closing

__RE_RESULT__ = re.compile("<b>([^<]*)</b>", re.I | re.S | re.M)

def go(fname):
    socket.setdefaulttimeout(120)

    data = json.load(open(fname))
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
            print u'[%s] %s' % (fname, m)

if __name__ == '__main__':

    glets = []
    for fs in sys.argv[1:]:
        for i in range(5):
            print '[%s] Spawn %d' % (fs, i)
            glets.append(gevent.spawn(go, fs))

    gevent.joinall(glets)

