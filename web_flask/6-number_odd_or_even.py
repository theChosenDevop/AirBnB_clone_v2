#!/usr/bin/python3
""" 6-number_odd_or_even module """

from flask import Flask
from flask import render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ displays 'number' followed by the value of n """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Render the html template """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Render html template if it is odd or even """
    if isinstance(n, int):
        if n % 2 == 0:
            return render_template('6-number_odd_or_even.html', n=n, num='even')
        else:
            return render_template('6-number_odd_or_even.html', n=n, num='odd')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
