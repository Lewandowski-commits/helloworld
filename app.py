from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

class User:
	def __init__(self, username='', password=''):
		self.username = username
		self.password = password

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
						query = {"username": user.username}):
			print("User found!")
		else:
			print("User foundn't")
		return redirect(url_for('index'))	
	return render_template('login.html', form=form)

@login_manager.user_loader
def load_user(user_id):
		return User.get(user_id)

@app.route('/xd')
def xd():
	return render_template('xd.html')

if __name__ == '__main__':
	app.run()
