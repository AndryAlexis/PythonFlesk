from flask import Blueprint, render_template

not_found_page = Blueprint("not_found", __name__, template_folder="./templates")

@not_found_page.app_errorhandler(404)
def not_found(error):
    data = {
        "title": "404",
        "message": "Not Found"
    }
    return render_template("404.html", data=data), 404