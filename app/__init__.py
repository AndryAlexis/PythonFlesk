from flask import Flask
# All pages
from .pages import *

def create_app():
    app = Flask(__name__, template_folder="./shared")

    # Register all pages
    app.register_blueprint(home_blueprint)
    app.register_blueprint(about_blueprint)
    app.register_blueprint(not_found_blueprint)

    return app