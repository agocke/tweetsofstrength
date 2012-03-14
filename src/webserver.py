import bottle

@bottle.route('/tos/hello')
def hello():
  return 'Hello, World!'

def main():
  bottle.run(host='0.0.0.0', port=8181)

if __name__ == '__main__':
  main()
