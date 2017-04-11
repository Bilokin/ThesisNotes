from bottle import route, run, template
@route('/')
def index():
    return '<center><h1>Well, hello anonymous!</h1></br><iframe width="560" height="315" src="https://www.youtube.com/embed/ER97mPHhgtM" frameborder="0" allowfullscreen></iframe></center>'

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='134.158.76.158', port=8080)
