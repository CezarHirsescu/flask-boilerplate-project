from flask import Blueprint, Response

views = Blueprint("views", __name__)

@views.route('/')
def index():
    return Response("<h1>your website is up and running!</h1>")