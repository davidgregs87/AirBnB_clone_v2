#!/usr/bin/python3
"""Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hbnb():
    """display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def Hbnb_1():
    """display “HBNB”"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def Hbnb_2(text):
    """“display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )”"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Hbnb_3(text):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route("/number/<int:n>", strict_slashes=False)
def Hbnb4(n):
    """display “n is a number” only if n is an integer"""
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def Hbnb5(n):
    """display “n is a number” only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def Hbnb6(n):
    """display “n is a number” only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run()
