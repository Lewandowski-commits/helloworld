from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/xd')
def xd():
	return render_template('xd.html')

if __name__ == '__main__':
	app.run()
