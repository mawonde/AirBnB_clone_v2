#!/usr/bin/python3
"""
A Flask web application with three routes: "/", "/hbnb", and "/c/<text>".
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
  """
    Display "C " followed by the value of the text variable
    """
  return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
  """
    Display "Python " followed by the value of the text variable.
    """
  return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
  """display “n is a number” only if n is an integer"""
  return "%d is a number" % n


if __name__ == '__main__':
  # Run the Flask app on 0.0.0.0:5000
  app.run(host='0.0.0.0', port=5000)
