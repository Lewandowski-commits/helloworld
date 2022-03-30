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
import datetime

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

class Post:
	def __init__(self, title, body, tags, author, date):
		self.title = title
		self.body = body
		self.tags = tags
		self.author = author
		self.date = date

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
	if 'username' in session:
		session.pop('username', None)
		flash('Logged out!', 'alert-primary')
	return redirect(url_for('index'))

@app.route('/blog', methods=['GET'])
def blog():
	posts = mongo.db.posts.find()
	return render_template('blog.html', posts=posts)

@app.route('/blog/new', methods=['GET', 'POST'])
def blog_new():
	if 'username' in session:
		from forms import NewPostForm
		form = NewPostForm(request.form)
		if request.method == 'POST' and form.validate():
			post = Post(form.title.data,
						form.body.data,
						form.tags.data,
						session['username'],
						datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
			# insert post
			inserted_post = mongo.db.posts.insert_one(
														{"title": post.title,
														"body": post.body,
														"tags": post.tags,
														"date": post.date
														}
													)
			flash(f'Post ID {inserted_post.inserted_id} added sucessfully!', 'alert-success')
		else:
			render_template('blog_new.html', form=form)
	else:
		flash('You need to log in before creating a new post', 'alert-warning')
		return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
		return User.get(user_id)

@app.route('/xd')
def xd():
	return render_template('xd.html')

if __name__ == '__main__':
	app.run()
