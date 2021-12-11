import flask
from flask import request, abort
from flask_cors import CORS, cross_origin
from solr.indexer_lsi import LSI
from solr_connection import SolrConnection
from news_api import news
from youtube import youtube
# from senti import sentiment
# from replies import replies
from tweetcounts import TweetCounts

# s = sentiment()
# r = replies()
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
    lsi_poi = LSI()
    get_news = news()
    cnt = TweetCounts()
    solr = SolrConnection()
    news_articles = []
    try:
        news_result = get_news.news(query)
        print(news_result)
        news_articles=news_result['articles'][:5]
    except:
        print("No news article found")
    # for article in news_result['articles']:
    #     results.append(article)

    wiki_text = ""
    wiki_url = ""
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

    tweets = lsi.query_execution(query)
    poi_tweets = lsi_poi.query_execution_poi(query)

    #Counts
    counts_gen = cnt.get_counts(tweets)
    counts_poi = cnt.get_counts(poi_tweets)
    tweets, total_rep_counts_gen = cnt.get_reply_counts(tweets)
    poi_tweets, total_rep_counts_poi = cnt.get_reply_counts(poi_tweets)


    res = flask.jsonify({
        'poi_tweets': poi_tweets,
        'tweets': tweets,
        'news': news_articles,
        'wiki': wiki_text,
        'wiki_url': wiki_url,
        'videos': video_urls,
        'gen_counts': counts_gen,
        'poi_counts': counts_poi,
        'total_gen_reply_counts': total_rep_counts_gen,
        'total_poi_reply_counts': total_rep_counts_poi
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
