#!/usr/bin/python3

"""
starts a Flask web application listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    return 'C %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '%d is number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        res = '%d is even' % n
    else:
        res = '%d is odd' % n
    return render_template('6-number_odd_or_even.html', result=res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
