import random, urllib2, xml.parsers.expat
from xml.dom.minidom import parseString
url = " http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=aa617e7f9009c45c38bbaa4f7fe50329&tags=kitten&safe_search=1&format=rest"
urltemplate = "http://farm%s.staticflickr.com/%s/%s_%s.jpg"

def getRandom():
    file = urllib2.urlopen(url)
    dom = parseString(file.read())
    photos = dom.getElementsByTagName('photos')[0]
    pages = photos.attributes['pages'].nodeValue

    perpage = int(photos.attributes['perpage'].nodeValue)
    kittyID = random.randint(0,perpage-1)
    newurl = url + "&page=" + str(random.randint(0,int(pages)-1))
    print newurl

    file2 = urllib2.urlopen(url)
    dom = parseString(file2.read())

    ourphoto = dom.getElementsByTagName('photo')[kittyID]
    farmid = ourphoto.attributes['farm'].nodeValue
    serverid = ourphoto.attributes['server'].nodeValue
    id = ourphoto.attributes['id'].nodeValue
    secret = ourphoto.attributes['secret'].nodeValue
    photourl = urltemplate%(farmid, serverid, id, secret)
    return photourl
