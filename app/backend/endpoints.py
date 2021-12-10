import flask
from flask import request, abort
from flask_cors import CORS, cross_origin
from solr.indexer_lsi import LSI
from solr_connection import SolrConnection
from news_api import news
from youtube import youtube
from senti import sentiment
from replies import replies
s = sentiment()
r = replies()
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

    wiki_text = ""
    try:
        wiki_text, wiki_url = solr.wiki(query)
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

    tweets, gen_country = lsi.query_execution(query)
    lsi_poi = LSI()

    poi_tweets, poi_country = lsi_poi.query_execution_poi(query)
    print(poi_tweets)
    for doc in poi_tweets:
        try:
            text = doc['tweet_text']
            sentiment, sentiment_score = s.analyze(text)
            doc['sentiment'] = sentiment
            doc['sentiment_score'] = sentiment_score
        except:
            print("key error")
    poi_tweets = r.fetch_replies(poi_tweets)
    print(poi_tweets)
    res = flask.jsonify({
        'poi_tweets':poi_tweets,
        'tweets': tweets,
        'news': news_articles,
        'wiki': wiki_text,
        'wiki_url': wiki_url,
        'videos': video_urls,
        'country_wise_poi': poi_country,
        'country_wise_gen': gen_country,
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
