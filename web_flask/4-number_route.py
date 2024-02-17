#!/usr/bin/python3
""" 4-number_route module """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ returns string output """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display HBNB as string output """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """ displays 'C' followed by the value of the text variable """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    """ displays 'Python' followed by the value of the text variable """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def display_number(n):
    """ displays 'number' followed by the value of n """
    n = int(n)
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
