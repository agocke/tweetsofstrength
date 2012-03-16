import collections
import cPickle
import functools
import string

Tweet = collections.namedtuple('Tweet',
                               ['text','user_id','user_name',
                                'date_tweeted','location'])

def load_tweets(path='all_tweets.pkl'):
  with open(path, 'rb') as f:
    return cPickle.load(f)
  return None


_last_search = None
def search_tweets(tweets, keyword, page=1):
  global _last_search
  if _last_search and _last_search[0] == keyword:
    remaining = _last_search[1]
  else:
    def output_stats(tweet):
      return tweet._asdict()
    remaining = [output_stats(t) for t in tweets if keyword in t.text]
    _last_search = (keyword, remaining)

  # Paginate
  if len(remaining) <= (page-1)*10:
    return "No more results"
  elif len(remaining) <= page*10:
    upper = len(remaining)
  else:
    upper = page*10
  return ({'proportion': (len(remaining), len(tweets)),
           'tweets': remaining[(page-1)*10:upper]})
