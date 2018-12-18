from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    user = {'username': 'Cray'}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Kisii!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie is bull!'
        },
        {
            'author': {'username': 'Boss'},
            'body': 'Nice deadlines!'
        },
        {
            'author': {'username': 'Troll'},
            'body': 'Im am just going to add a lot of text to see how multiple lines are rendered in this html. Also, please remember that I am not trolling, because every troll who ever lived identified themselves as a troll. But then again, did I ever live? Ahahahahaaha, snicker, snicker, snicker!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
