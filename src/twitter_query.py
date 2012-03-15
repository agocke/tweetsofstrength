import collections
import cPickle
import functools

Tweet = collections.namedtuple('Tweet',
                               ['text','user_id','user_name',
                                'date_tweeted','location'])

def load_tweets(path='all_tweets.pkl'):
  with open(path, 'rb') as f:
    return cPickle.load(f)
  return None

def search_tweets(tweets, keyword):
  return [t for t in tweets if keyword in t.text]
