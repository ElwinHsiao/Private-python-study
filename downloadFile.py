import urllib2, sys
import os
from urlparse import urlsplit


def guessfilenamebyheader(info):
    localName = info['Content-Disposition'].split('filename=')[1]
    if localName[0] == '"' or localName[0] == "'":
        return localName[1:-1]

def guessfilenamebyurl(url):
    return os.path.basename(urlsplit(url)[2])

def download(url, localFileName = None):
    localName = guessfilenamebyurl(url)
    req = urllib2.Request(url)
    print 'waiting for download...'
    r = urllib2.urlopen(req)
    if r.info().has_key('Content-Disposition'):
        # If the response has Content-Disposition, we take file name from it
        localName = guessfilenamebyheader(r.info())
    elif r.url != url: 
        # if we were redirected, the real file name we take from the final URL
        localName = guessfilenamebyurl(r.url)
    if not os.path.splitext(localName)[1]:
        localName += r'.txt'
    if localFileName: 
        # we can force to save the file as specified name
        localName = localFileName
    print 'write to file: %s\%s' % (os.getcwd(), localName) 
    os
    f = open(localName, 'wb')
    f.write(r.read())
    f.close()


leng = len(sys.argv)
filename = None
if leng <= 1:
    raise RuntimeError('you must give the url')
elif leng == 2:
    url = sys.argv[1]
else:
    url = sys.argv[2]
    filename = sys.argv[1]
##print url, filename
download(url, filename)
