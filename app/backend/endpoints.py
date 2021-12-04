import flask
from flask import request, abort
from flask_cors import CORS, cross_origin
from solr.indexer_lsi import LSI
from solr_connection import SolrConnection
from news_api import news
from youtube import youtube
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

    lsi = LSI()
    get_news = news()
    news_result = get_news.news()
    results = []
    solr = SolrConnection()
    for i in range(5):
        results.append(news_result['articles'][i])
    wiki_text = solr.wiki(query)


    yt = youtube()
    video_urls = yt.fetch_videos(query)


    res = flask.jsonify({'tweets': lsi.query_execution(query)})
    return res


@app.errorhandler(400)
def direction_err(e):
    return e.description, 400


@app.route('/api/ping', methods=['GET'])
def ping():
    _dict = {'success': 'true'}
    return _dict


app.run()
