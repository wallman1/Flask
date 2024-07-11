from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Moose'}
    posts = [
        {
            'author': {'username': 'Reggie'},
            'body': 'Ruff, ruff!'
        },
        {
            'author': {'username': 'Fallon'},
            'body': 'Awooooooooo!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/no_title')
def no_title():
    user = {'username': 'Moose'}
    return render_template('index.html', user=user)