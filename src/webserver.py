from __future__ import print_function

import bottle
import json
import sys

import twitter_query

_TWEETS = None

@bottle.route('/tos/hello')
def hello():
  return 'Hello, World!'

@bottle.route('/tos/tweets/<keyword:re:\w+>')
@bottle.route('/tos/tweets/<keyword:re:\w+>/<page:int>')
def get_tweets(keyword, page=1):
  filtered = twitter_query.search_tweets(_TWEETS, keyword)
  if len(filtered) <= (page-1)*10:
    return "No more results"
  elif len(filtered) <= page*10:
    upper = len(filtered)
  else:
    upper = page*10
  return json.dumps([t._asdict() for t in filtered[(page-1)*10:upper]])

def main():
  global _TWEETS
  if len(sys.argv) > 1:
    _TWEETS = twitter_query.load_tweets(sys.argv[1])
  else:
    _TWEETS = twitter_query.load_tweets()
  if not _TWEETS:
    print("Couldn't load tweet pickle, exiting.", file=sys.stderr)
  else:
    bottle.run(host='localhost', port=8181)

if __name__ == '__main__':
  main()
