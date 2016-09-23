__author__ = 'Varun'

from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

'''
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Raingod'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!',
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'Arrested Development was a ROFLMAO funny series!',
        },
    ]
    return render_template('index.html', title='Raingod\'s Home', user=user, posts=posts)
'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Raingod\'s Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])