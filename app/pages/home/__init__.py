from flask import Blueprint, render_template

home_page = Blueprint("home", __name__, template_folder='./templates')

@home_page.route("/")
def page():
    data = {
        "title": "WhatEELS | Home",
    }
    return render_template("index.html", data=data)