import urllib
import xml.etree.ElementTree as ET

while True:
    url = 'http://python-data.dr-chuck.net/comments_42.xml'
    print 'Retrieving', url
    if len(url) < 1 : break
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)
