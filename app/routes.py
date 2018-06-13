from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Adam'}
    posts = [
        {
            'author': {'username': 'AJ'},
            'body': 'Test'
        },
        {
            'author': {'username': 'Joe'},
            'body': 'Testing123'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
