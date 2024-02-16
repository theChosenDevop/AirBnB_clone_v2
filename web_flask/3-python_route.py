#!/usr/bin/python3
"""This is the 3-python_route module"""

from flask import Flask
"""Defines the imported modules"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hello hbnb home page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """another hbnb page hi!"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
    """uses the text variable redirect"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Pythone text variable redirect"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
