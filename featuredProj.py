import urllib2
import json

featureID = 774437
key = "DONORSCHOOSE"
def parse(id):
    results = urllib2.urlopen("http://api.donorschoose.org/common/json_feed.html?id=%d&APIKey=%s"%(id,key))
    rdict = json.loads(results.read())
    return rdict["proposals"][0]["imageURL"]
