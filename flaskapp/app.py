import os
import sys
import json

from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('main.html')

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
