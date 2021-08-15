import flask
from .models import DistanceResult
from flask import Blueprint, render_template, request

locator = Blueprint('locator', __name__, )

@locator.route("/locator", methods=["GET", "POST"])
def index():
    """A distance locator endpoint.
    ---
    get:
      description: Get a default page with the form to input
      responses:
        200:
          content:
            html
    post:
      description: Calculate distance between points and open a new form to input
      responses:
        200:
          content:
            html
    """
    distance_result = DistanceResult()

    if flask.request.method == "POST":
        lat_orig = float(request.form.get('lat_orig'))
        lng_orig = float(request.form.get('lon_orig'))
        lat_dest = float(request.form.get('lat_dest'))
        lng_dest = float(request.form.get('lon_dest'))
        
        distance_result = DistanceResult(lat_orig, lng_orig, lat_dest, lng_dest)  
        distance_result.save_history()

    history = DistanceResult.load_history()
    print(history)
    return render_template("locator/index.html", distance_result=distance_result, history=history)





