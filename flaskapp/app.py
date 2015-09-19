import os
import json
from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('referenceindex.html')

if __name__ == '__main__':
    app.run(debug=True)
