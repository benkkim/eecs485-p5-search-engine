"""main.py"""
import flask
import search
# import threading
# import pathlib

@search.app.route('/', methods=['GET'])
def search():
    return flask.render_template('index.html')

# Search server backend makes REST API requests to each Index server
# and combines the results from each inverted index segment.

# It should make these requests in parallel threads.
# The Search server then displays the top 10 results to the client.
