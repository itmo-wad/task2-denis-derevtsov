"""
App initialization file.
Imports and initializes its main components.
"""

from flask import Flask
from config import Config 		# Project configuration import


# Create Flask app, load app.config
app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = '1234567890abdfdfccdb123456789012'

import views
