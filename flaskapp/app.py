import os
import sys
import json
from flask import Flask, request, redirect, render_template, url_for
import sys
# sys.path.append('~/thugcorpthenorth/src')
# import application

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('main.html')

@app.route('/results')
def index():
    description = "Toronto"
    latitude = "43.6529206"
    longitude = "-79.3849008"
    # results = application.run_clusters(latitude, longitude, radius, theme) 
    results=[   {'name': "Casa Loma", 'address': "132 INSERT ADDRESS HERE", 'latitude': 43.67811065, 'longitude': -79.4094081263767},
                {'name': "Mt Pleasant Cemetery", 'address': "132 addrrrrr", 'latitude': 43.6973726, 'longitude': -79.379036798564},
                {'name': "The Opera House", 'address': "132 pls address", 'latitude': 43.6532260, 'longitude': -79.3831840}
             ]

    return render_template('map_results.html', description=description, latitude=latitude, longitude=longitude, results=results)


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
