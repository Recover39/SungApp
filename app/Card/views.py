from flask import Blueprint, render_template, request, redirect

card = Blueprint('Card', __name__, url_prefix='/card')

@card.route('/')
def index():
    return render_template('main.jade')

@card.route('/add', methods=['GET','POST'])
def write():
    if request.method == 'POST':
        print(request.form['body'])
    return redirect('/card')