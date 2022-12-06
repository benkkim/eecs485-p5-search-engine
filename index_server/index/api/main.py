import flask 

app = flask.Flask(__name__)

@app.route('.api/v1', methods=['GET'])
def get_page():
    context = {
        "hits": "/api/v1/hits",
        "url": "/api/v1/"
    }
    return flask.jsonify(**context)

@app.route('/api/v1/hits/', methods=['GET'])
def get_hits():
    """Get hits for a query."""
    query = flask.request.args.get('q', default='', type=str)
    w = flask.request.args.get('w', default=0.5, type=float)

    context = {
        "hits": [{docid: <docid>, score: <score>}]
    }
    # Return hits
    return flask.jsonify(**context)