from __future__ import print_function

import bottle
import json
import os
import sys

import twitter_query

_TWEETS = None

@bottle.route('/tos/hello')
def hello():
  return 'Hello, World!'


@bottle.route('/tos/static/<filepath:path>')
def serve_static(filepath):
  return bottle.static_file(filepath,
                            root=os.path.join(os.path.dirname(__file__),
                                              'static'))


@bottle.route('/tos/tweets/<keyword>')
@bottle.route('/tos/tweets/<keyword>/<page:int>')
def get_tweets(keyword, page=1):
  return json.dumps(twitter_query.search_tweets(_TWEETS, keyword))


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
