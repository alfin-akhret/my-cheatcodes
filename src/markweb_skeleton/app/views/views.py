# Basic Views
from flask import Blueprint

default = Blueprint('default', __name__)

@default.route('/')
def home():
    return 'Welcome to Markweb'