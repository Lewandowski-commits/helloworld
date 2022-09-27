"""Routes for parent Flask app."""
from flask import render_template, send_from_directory
from flask import current_app as app
import os

@app.route('/')
def home():
    """Landing page."""
    companies = ['lingaro', 'haleon', 'gsk']

    return render_template(
        'index.html',
        companies=companies
    )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')