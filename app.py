from binhex import Error
from logging.handlers import RotatingFileHandler
import logging
from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_login import LoginManager
from flask_pymongo import PyMongo
from urllib.parse import quote
from pymongo.errors import OperationFailure

app = Flask(__name__)

# logging
handler = RotatingFileHandler(os.path.join(app.root_path, 'logs', 'error_log.log'), maxBytes=102400, backupCount=10)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')

handler.setFormatter(logging_format)
app.logger.addHandler(handler)

# app, login manager and pymongo config
app.secret_key = os.getenv('FLASK_SECRET')
app.config['MONGO_URI'] = f'mongodb+srv://{quote(str(os.getenv("MONGODB_USER")))}:{quote(str(os.getenv("MONGODB_PASSWORD")))}@cluster0.uivfa.mongodb.net/blog?retryWrites=true&w=majority'
mongo = PyMongo(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User:
	def __init__(self, username='', password=''):
		self.username = username
		self.password = password

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)

    return render_template('error.html', error=error)

@app.errorhandler(500)
def special_exception_handler(error):
    app.logger.error(error)
    return render_template('error.html', error=error)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	from forms import LoginForm
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		user = User(form.username.data,
					form.password.data)
		# ask DB if credentials are ok
		if mongo.db.users.find_one({"username": user.username,
								"password": user.password}):
			session['username'] = user.username
			flash('Logged in!', 'alert-primary')
			return redirect(url_for('index'))
		else:
			flash('Wrong username and/or password!', 'alert-warning')
	return render_template('login.html', form=form)

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
		return User.get(user_id)

@app.route('/xd')
def xd():
	return render_template('xd.html')

if __name__ == '__main__':
	app.run()
