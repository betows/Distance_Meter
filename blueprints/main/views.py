from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder="templates")

@main.route("/")
def index():
    """Home page endpoint.
    ---
    get:
      description: Get a home page
      responses:
        200:
          content:
            html
    """
    return render_template("main/index.html")