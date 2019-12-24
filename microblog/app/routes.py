from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'User'}
    posts = [
        {
            'author': {'username': 'Bill'},
            'body': 'Building with Python'
        },
        {
            'author': {'username': 'Scott'},
            'body': 'Azure the cloud of the future'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)