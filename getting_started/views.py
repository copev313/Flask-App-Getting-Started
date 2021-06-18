from flask import request, render_template, redirect, url_for
from getting_started import app


# Home Page:
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# 404 Page Not Found:
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# Route so we can test 404 page:
@app.route('/404')
def page_not_found():
    return render_template('404.html')
