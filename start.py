import hmac
import hashlib
import urllib2
import json
import timestring
import requests
from pprint import pprint
from eventObject import eventObject

import sys
reload(sys)
sys.setdefaultencoding('utf8')

api_key    = 'V37UcPDfsVDiaYgs'
secret_key = 'yOjBov7vc-0op26qkHmaLOL4abzb34oK'
festival   = 'fringe'
query      = '/events?festival=' + festival + '&year=2019&key=' + api_key

signature  = hmac.new(secret_key, query, hashlib.sha1).hexdigest()
url        = \
'https://api.edinburghfestivalcity.com' + query + '&signature=' + signature

response = requests.get(url)
data = json.loads(response.text)
for x in data:
  try:
    pprint(eventObject(x))
    print ""
  except:
    print(eventObject(x))
