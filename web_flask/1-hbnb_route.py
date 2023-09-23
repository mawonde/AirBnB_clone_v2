#!/usr/bin/python3
"""
A Flask web application that displays "Hello HBNB!" and "HBNB" on two different routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
  """
    Displays "Hello HBNB!" when accessed.
    """
  return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
  """
    Displays "HBNB" when accessed.
    """
  return "HBNB"


if __name__ == '__main__':
  # Run the Flask app on 0.0.0.0:5000
  app.run(host='0.0.0.0', port=5000)
