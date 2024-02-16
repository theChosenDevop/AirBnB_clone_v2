#!/usr/bin/python3
"""This is the 2-c_route module"""

from flask import Flask, escape
"""This defines the imported modules"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
    # Replace underscores with spaces
    formatted_text = escape(text).replace('_', ' ')
    return f"C {formatted_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
