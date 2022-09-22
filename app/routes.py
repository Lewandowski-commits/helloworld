"""Routes for parent Flask app."""
from flask import render_template
from flask import current_app as app
import boto3

client = boto3.client('dynamodb')

dynamodb = boto3.resource('dynamodb')

positions = dynamodb.Table('job_history').scan()['Items']

@app.route('/')
def home():
    """Landing page."""
    return render_template(
        'index.html',
        positions=positions
    )