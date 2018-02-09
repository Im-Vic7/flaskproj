from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user
from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')
