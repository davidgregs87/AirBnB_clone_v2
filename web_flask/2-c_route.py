#!/usr/bin/python3
"""Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition"""

from flask import Flask, render_template_string
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


if __name__ == '__main__':
    app.run()
