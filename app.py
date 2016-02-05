from flask import Blueprint, render_template

default_page = Blueprint('default_page', __name__, template_folder='templates')

@default_page.route("/")
def home():
    return render_template('home.html')

