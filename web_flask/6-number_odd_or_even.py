#!/usr/bin/python3
"""This is the 3-python_route module"""

from flask import Flask, render_template
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
    """Python text variable redirect"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def check_number(n):
    """check number and print it if it is an int"""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Render the html templet"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Is the number odd or even, display web accordingly"""
    ev_or_od = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, ev_or_od=ev_or_od)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
