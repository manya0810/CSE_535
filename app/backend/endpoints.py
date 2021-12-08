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
    solr = SolrConnection()
    news_articles=[]
    try:
        news_result = get_news.news(query)
        print(news_result)
        news_articles=news_result['articles'][:5]
    except:
        print("No news article found")
    # for article in news_result['articles']:
    #     results.append(article)

    wiki_text=""
    try:
        wiki_text,wiki_url = solr.wiki(query)
        print(wiki_text)
    except:
        print("Wiki failed")

    yt = youtube()
    video_urls = ""
    try:
        video_urls = yt.fetch_videos(query)
        print(video_urls)
    except:
        print("youtube failed")

    tweets = lsi.query_execution(query)

    res = flask.jsonify({
        'tweets': tweets,
        'news': news_articles,
        'wiki': wiki_text,
        'videos': video_urls
    })
    return res


@app.errorhandler(400)
def direction_err(e):
    return e.description, 400


@app.route('/api/ping', methods=['GET'])
def ping():
    _dict = {'success': 'true'}
    return _dict


app.run()
