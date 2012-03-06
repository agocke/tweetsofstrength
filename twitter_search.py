import json
import pycurl
import urllib

class TwitterStreamClient(object):
  def __init__(self, topics, callback):
    with open('twitter_auth.json', 'r') as auth_f:
        auth = json.load(auth_f)
    self.callback = callback
    self.buf = ''

    conn = pycurl.Curl()
    conn.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
    conn.setopt(pycurl.USERPWD, '{0}:{1}'.format(auth['user'],
                                               auth['password']))
    conn.setopt(pycurl.URL, 'https://stream.twitter.com/1/statuses/filter.json')
    conn.setopt(pycurl.POSTFIELDS, urllib.urlencode(dict(track=topics)))
    conn.setopt(pycurl.WRITEFUNCTION, self.got_data)
    conn.perform()

  def got_data(self, data):
    self.buf += data
    if data.endswith('\r\n') and self.buf.strip():
      content = json.loads(self.buf)
      self.buf = ''
      self.callback(content)


if __name__ == '__main__':
  def callback(content):
    print content
  client = TwitterStreamClient('primary', callback)
