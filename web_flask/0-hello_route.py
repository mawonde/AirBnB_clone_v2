#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


# Define the route with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
  """ Displays "Hello HBNB!" when accessed. """
  return "Hello HBNB!"


if __name__ == '__main__':
  # Run the Flask app on 0.0.0.0:5000
  app.run(host='0.0.0.0', port=5000)
