#!/usr/bin/python3
""" This is the 0-hello_route module """

from flask import Flask
""" import Flask module from flask package """

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ returns a string output """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
