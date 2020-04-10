""" Views file """

from flask import render_template, send_from_directory
from app import app


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html', title='Papug Memes Gallery', pics_quantity=45)


# Returns images used on the main page
@app.route('/img/<path:filename>')
def static_img(filename):
	return send_from_directory('static/content/pics/', filename)


# Returns custom JS/CSS files
@app.route('/static/<path:filename>')
def static_css(filename):
    return send_from_directory('static/',filename)
