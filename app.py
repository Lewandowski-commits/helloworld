from logging.handlers import RotatingFileHandler
import logging
import os
from flask import Flask, render_template, request, url_for, redirect, session
from flask_login import LoginManager

app = Flask(__name__)

# logging
handler = RotatingFileHandler(os.path.join(app.root_path, 'logs', 'error_log.log'), maxBytes=102400, backupCount=10)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')

handler.setFormatter(logging_format)
app.logger.addHandler(handler)

app.secret_key = os.getenv('FLASK_SECRET')
login_manager = LoginManager()
login_manager.init_app(app)

class User:
	def __init__(self, username='', password=''):
		self.username = username
		self.password = password

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)

    return 'This page does not exist', 404


@app.errorhandler(500)
def special_exception_handler(error):
    app.logger.error(error)
    return '500 error', 500

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	from forms import LoginForm
	from db import Db
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		user = User(form.username.data,
					form.password.data)
		# ask DB if credentials are ok
		db = Db()
		if db.find_one(collection = "users",
						query = {"username": user.username,
								"password": user.password}):
			print("User found!")
			session['username'] = user.username
		else:
			print("User foundn't")
		return redirect(url_for('index'))	
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
