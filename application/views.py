from application import app

@app.route('/')
@app.route('/hi')
@app.route('/index')
def hi():
	return '<h1>HI !!!</h1>'