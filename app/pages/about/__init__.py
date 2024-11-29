from flask import Blueprint, render_template, request

about_page = Blueprint("about", __name__, template_folder="./templates")

@about_page.route("/about/<name>/<int:age>")
def about(name, age):
    data = {
        "title": "About",
        "name": name,
        "age": age
    }
    print(request.args.get('status', 'No status'))
    return render_template("about.html", data=data)