from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('main.jade')

@app.route('/test')
def test():
    return render_template('testMain.jade')

@app.route('/testForm')
def testForm():
    return render_template('testHTML.html')

