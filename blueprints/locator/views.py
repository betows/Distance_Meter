from flask import Blueprint, render_template, request
from geopy.distance import geodesic 

locator = Blueprint('locator', __name__,)


@locator.route("/locator")
def index():
    return render_template("locator/index.html")


@locator.route("/locator/result", methods=["POST"])
def result():    
    origin_latitude = request.form.get('lat_orig')
    origin_longitude = request.form.get('lon_orig')
    destination_latitude = request.form.get('lat_dest')
    destination_longitude = request.form.get('lon_dest')
    
    coords_1 = (origin_latitude, origin_longitude)
    coords_2 = (destination_latitude, destination_longitude)
    print(coords_1)
    print(coords_2)
    distance = geodesic(coords_1, coords_2).km

    return render_template("locator/result.html", distance=distance)