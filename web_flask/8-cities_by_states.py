#!/usr/bin/python3
"""
Flask Web Application Module for Cities by States

This module creates a Flask web application that displays a list of cities grouped by states.
It demonstrates the use of Flask for web serving and integration with a storage system for
retrieving State and City data.

Routes:
    /cities_by_states: Renders an HTML page listing all cities grouped by states.

Usage:
    Run this script directly to start the Flask development server:
    $ python3 8-cities_by_states.py

    The server will start on http://0.0.0.0:5000/

Dependencies:
    - Flask: Web framework for serving the application
    - models: Custom module for data storage and retrieval

Note:
    This script assumes the existence of a storage system and State model in the models module.
    It also requires a template file named '8-cities_by_states.html' for rendering the page.

Author: [Your Name]
Date: [Current Date]
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states')
def states_list():
    """
    Render the cities_by_states page.

    Returns:
        str: Rendered HTML page with list of states and their cities.
    """
    path = '8-cities_by_states.html'
    states = storage.all('State')
    return render_template(path, states=states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """
    Clean-up the session after each request.

    Args:
        arg: Not used, kept for consistency with Flask's teardown_appcontext decorator.
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
