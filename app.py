from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/xd')
def xd():
	return 'xDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'

if __name__ == '__main__':
	app.run()
