
import json
import urllib
import urllib2

def search_twitter(search_url_string='http://search.twitter.com/search.json?q={}'):
  search_json = urllib2.urlopen(SEARCH_URL_STRING.format(urllib.quote('primaries vote')))
  search_decode = json.loads(search_json.read())
  return search_decode
