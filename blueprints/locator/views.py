import flask
from flask import Blueprint, render_template, request
from geopy.distance import geodesic

locator = Blueprint('locator', __name__, )


@locator.route("/locator", methods=["GET", "POST"])
def index():
    """
    Calculate distance information got from the api using geodesic package and show to the user
    """
    distance = None
    destination_latitude = None
    destination_longitude = None

    if flask.request.method == "POST":
        origin_latitude = request.form.get('lat_orig')
        origin_longitude = request.form.get('lon_orig')
        destination_latitude = request.form.get('lat_dest')
        destination_longitude = request.form.get('lon_dest')

        coords_1 = (origin_latitude, origin_longitude)
        coords_2 = (destination_latitude, destination_longitude)
        distance = round(geodesic(coords_1, coords_2).km)

    return render_template("locator/index.html", distance=distance,
                                                 destination_longitude=destination_longitude,
                                                 destination_latitude=destination_latitude)
