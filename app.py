from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	from forms import LoginForm
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		user = User(form.username.data,
					form.password.data)
		# ask DB if credentials are ok
		return redirect(url_for('/'))	
	return render_template('login.html', form=form)

@app.route('/xd')
def xd():
	return render_template('xd.html')

if __name__ == '__main__':
	app.run()
