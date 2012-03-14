import bottle

@bottle.route('/tweetsofstrength/hello')
def hello():
  return 'Hello, World!'

def main():
  bottle.run(host='unix:///tmp/tos.sock')

if __name__ == '__main__':
  main()
