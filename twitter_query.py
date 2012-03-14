import collections
import cPickle
import guess_language

Tweet = collections.namedtuple('Tweet',
                               ['text','user_id','user_name',
                                'date_tweeted','location'])

def process_tweets():
    f1 = open('all_tweets.pkl', 'rb')
    f2 = open('new_tweets.pkl', 'wb')
    all_tweets = cPickle.load(f1)
    new_tweets = []
    for i in xrange(len(all_tweets)):
        if i % 10000 == 0:
            print 'Processing tweet ', i
        try:
            if guess_language.guessLanguage(all_tweets[i].text) == 'en':
                new_tweets.append(all_tweets[i])
        except Exception:
            pass
    f1.close()
    cPickle.dump(new_tweets, f2)
    f2.close()

if __name__ == '__main__':
    process_tweets()
