import datetime
import sqlite3
import twitter_search


def main():
  with open('topics.txt', 'r') as topics_f:
    topics = topics_f.read()
  topics = ','.join(l.strip() for l in topics.splitlines())

  sqlite_path = 'tweets.db'
  db_conn = sqlite3.connect(sqlite_path)
  client = twitter_search.TwitterStreamClient(topics, write_to_sqlite(db_conn))

def write_to_sqlite(db_conn):
  def callback(content):
    if content['user']['lang'] == 'en':
      text = content['text']
      user_id = content['user']['id']
      user_name = content['user']['screen_name']
      date = datetime.datetime.strptime(content['created_at'],
                                        '%a %b %d %H:%M:%S +0000 %Y')
      location = content['user']['location']
      with db_conn:
        db_conn.execute('INSERT INTO tweets VALUES (NULL,?,?,?,?,?);',
                        (content['text'],
                         content['user']['id'],
                         content['user']['screen_name'],
                         date.isoformat(),
                         content['user']['location']))

  return callback

if __name__ == '__main__':
  main()
