from flask import Blueprint, render_template

card = Blueprint('Card', __name__, url_prefix='/card')

@card.route('/')
def index():
    return render_template('main.jade')