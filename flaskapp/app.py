import os
import sys
import json
from flask import Flask, request, redirect, render_template, url_for
import sys
import application
from geopy.geocoders import Nominatim
import geo_results

app = Flask(__name__)
sys.path.append('../src')
geolocator = Nominatim()

@app.route('/')
def homepage(location=None):
    return render_template('index.html', location=location)

#, methods=['POST']
@app.route('/results', methods=['POST'])
def index():
    error = None
    (address, coordinates) = geolocator.geocode(request.form['location'])

    latitude = coordinates[0]
    longitude = coordinates[1]
    radius = float(request.form['distance'])*1000
    theme = request.form['find']
    results = application.run_clusters(latitude, longitude, radius, theme)
    return render_template('map_results.html', radius=radius, latitude=latitude, longitude=longitude, results=results)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == '__main__':
    app.run(debug=True)
