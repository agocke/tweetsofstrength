from bottle import route,run

@route('/tweetsofstrength/hello')
def hello():
  return 'Hello, World!'

run(host='localhost', port=8181)
