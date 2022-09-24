"""Routes for parent Flask app."""
from flask import render_template
from flask import current_app as app

@app.route('/')
def home():
    """Landing page."""
    companies = ['lingaro', 'haleon', 'gsk']

    return render_template(
        'index.html',
        companies=companies
    )