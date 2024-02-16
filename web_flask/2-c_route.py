#!/usr/bin/python3
"""This is the 2-c_route module"""

from flask import Flask
"""This defines the imported modules"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hello hbnb method"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb page home page"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
    """Special dynamic text page"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
