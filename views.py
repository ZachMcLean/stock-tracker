from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


# basically this setting up a blueprint so we can access home at url.com/view

# Templates are nice because you can pass variables from python
# to the rendered html page like a JS templated String
@views.route("/")
def home():
    return render_template("index.html", name="Zach")

@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name=username)
