from flask import Blueprint, render_template, request

card = Blueprint('Card', __name__, url_prefix='/card')

@card.route('/')
def index():
    return render_template('main.jade')

@card.route('/add', method=['POST'])
def write_card():
    json = request.json
    print(json)