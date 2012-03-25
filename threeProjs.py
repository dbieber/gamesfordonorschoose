import urllib2
import json

featureID = 774437
key = "DONORSCHOOSE"
def parse():
    projects = []
    results = urllib2.urlopen("http://api.donorschoose.org/common/json_feed.html?sortBy=1&APIKey=%s"%(key))
    rdict = json.loads(results.read())
    return rdict["proposals"][0:3]
