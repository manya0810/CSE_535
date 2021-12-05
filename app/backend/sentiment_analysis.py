import json
import urllib.request
from transformers import pipeline
from indexer import Indexer
from googletrans import Translator
from deep_translator import GoogleTranslator


class SentimentAnalysis:
    def __init__(self):
        self.classifier = pipeline('sentiment-analysis')
        self.translator = Translator()

    def perform_sentiment_analysis(self):
        solr_query = "http://ec2-52-72-185-101.compute-1.amazonaws.com:8983/solr/BM25_Project_4/select?q.op=OR&q=*%3A*&rows=461761&start=1239"
        data = urllib.request.urlopen(solr_query)
        docs = json.load(data)['response']['docs']
        indexer = Indexer()
        for document in docs:
            text_en = document["tweet_text"]
            text_en = GoogleTranslator(source='auto', target='en').translate(text_en)
            if (len(text_en) > 512):
                text_en = text_en[:512]
            classifier_result = self.classifier(text_en)
            sentiment = classifier_result[0]['label']
            sentiment_score = classifier_result[0]['score']
            document['sentiment'] = sentiment
            document['sentiment_score'] = sentiment_score
            document.pop('_version_')
            indexer.create_documents(document)

if __name__ == "__main__":
    sentiment_analysis = SentimentAnalysis()
    sentiment_analysis.perform_sentiment_analysis()