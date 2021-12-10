from CSE_535.solr.indexer_lsi import LSI
import urllib.request
import json
from senti import sentiment
s = sentiment()
class replies:
    def fetch_replies(self,poi_tweets):
        for i in poi_tweets:
            id = i['id']
            solr_query = "http://ec2-52-72-185-101.compute-1.amazonaws.com:8983/solr/BM25_Sentiment_Analysis_V1/select?q.op=OR&q=replied_to_tweet_id%3A" + id + "&rows=30"
            data = urllib.request.urlopen(solr_query)
            docs = json.load(data)['response']['docs']
            for doc in docs:
                try:
                    text = doc['reply_text']
                    sentiment, sentiment_score = s.analyze(text)
                    doc['sentiment'] = sentiment
                    doc['sentiment_score'] = sentiment_score
                    #print(doc)
                except:
                    print("key error")

            i['replies'] = docs
        return poi_tweets
        #print(poi_tweets)

# r = replies()
# poi_tweets = [{
#     "poi_name": "POTUS",
#     "poi_id": 1349149096909668363,
#     "country": "USA",
#     "id": "1436366944886837260",
#     "tweet_text": "My message to unvaccinated Americans is this: What more is there to wait for? What more do you need to see?\n\nWe hav… https://t.co/TBP0YSKIxX",
#     "tweet_lang": "en",
#     "text_en": "My message to unvaccinated Americans is this: What more is there to wait for? What more do you need to see?\n\nWe hav… https://t.co/TBP0YSKIxX",
#     "tweet_urls": ["https://t.co/TBP0YSKIxX"],
#     "tweet_date": "2021-09-10T17:00:00Z",
#     "verified": True,
#     "_version_": 1718191633727488002}]
#
# r.fetch_replies(poi_tweets)