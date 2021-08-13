# importing required libraries
import requests, json
import googlemaps


# enter your api key here
api_key = 'your_api_key'

# Take source as input
source = input("Coordenadas origem:")

# Take destination as input
dest = input("Coordenadas destino:")

# url variable store url
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

# Get method of requests module
# return response object
r = requests.get(url + 'origins=' + source +
             '&destinations=' + dest +
             '&key=' + api_key)

# json method of response object
# return json format result
x = r.json()

# by default driving mode considered

# print the value of x
print(x)


# Requires API key
gmaps = googlemaps.Client(key='your_api_key')

# Requires cities name
my_dist = gmaps.distance_matrix('Delhi', 'Mumbai')['rows'][0]['elements'][0]

# Printing the result
print(my_dist)
