import flask
from flask import request, abort
from flask_cors import CORS, cross_origin
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query')

    if query is None:
        abort(400, {'error': 'query parameter is required'})

    poi = request.args.get('poi')
    country = request.args.get('country')
    language = request.args.get('language')
    topic = request.args.get('topic')

    tweets = [{"id": 1437572262568226816, "poi_name": "KCPubHealth", "poi_id": 145036955, "verified": True, "tweet_text": "Join us this week at a #COVID19 Vaccination Pop-up Event in @KingCountyWA near you!\n\nFor time, location, and all other event details, go to: https://t.co/Cm6jnYoHpG\n\n#ivax2protect #CovidResources #KingCounty #GetVaccinated #Delta #CovidVaccine https://t.co/5GU3UQzAfo", "tweet_lang": "en", "hashtags": ["COVID19", "ivax2protect", "CovidResources", "KingCounty", "GetVaccinated", "Delta", "CovidVaccine"], "mentions": ["KingCountyWA"], "tweet_date": "2021-09-14 00:00:00", "country": "USA", "text_en": "Join us this week at a Vaccination Pop-up Event in near you!For time, location, and all other event details, go to:"}]
    res = flask.jsonify({'tweets': tweets})
    # res.headers.add('Access-Control-Allow-Origin', '*')
    return res


@app.errorhandler(400)
def direction_err(e):
    return e.description, 400


@app.route('/api/ping', methods=['GET'])
def ping():
    _dict = {'success': 'true'}
    return _dict


app.run()
