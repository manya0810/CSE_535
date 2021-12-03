import flask
from flask import request, abort
from flask_cors import CORS, cross_origin
from solr_connection import SolrConnection
#import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query')

    if query is None:
        abort(400, {'error': 'query parameter is required'})

    solr = SolrConnection()
    wiki_text = solr.wiki(query)
    res = flask.jsonify({'tweets': solr.convert_query(query)})
    return res


@app.errorhandler(400)
def direction_err(e):
    return e.description, 400


@app.route('/api/ping', methods=['GET'])
def ping():
    _dict = {'success': 'true'}
    return _dict


app.run()
