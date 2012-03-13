import collections

Tweet = collections.namedtuple('Tweet',
                               ['text','user_id','user_name',
                                'date_tweeted','location'])
