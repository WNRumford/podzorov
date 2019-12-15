from flask import Flask
from config import Config, ProdConfig, DevConfig

app = Flask(__name__)

app.config.from_object('config.DevelopConfig')

@app.route('/hi')
def hello():
	return '<h1>Hello !!!</h1>'

if __name__ == '__main__':
	app.run(debug=True)
