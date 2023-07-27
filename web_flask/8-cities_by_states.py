#!/usr/bin/python3
'''A flask application'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''Return all city instance by referencing with state id'''
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown(exception):
    """close connection"""
    storage.close()

if __name__ == '__main__':
    app.run()