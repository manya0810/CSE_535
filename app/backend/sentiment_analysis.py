import json
import urllib.request
from transformers import pipeline
from indexer import Indexer
from googletrans import Translator

class SentimentAnalysis:
    def __init__(self):
        self.classifier = pipeline('sentiment-analysis')
        self.translator = Translator()

    def perform_sentiment_analysis(self):
        solr_query = "http://ec2-52-72-185-101.compute-1.amazonaws.com:8983/solr/BM25_Project_4/select?q.op=OR&q=*%3A*&rows=461761"
        data = urllib.request.urlopen(solr_query)
        docs = json.load(data)['response']['docs']
        final_documents = []
        for document in docs:
            text_en = self.translator.translate(document["tweet_text"], dest='en')
            classifier_result = self.classifier(text_en)
            sentiment = classifier_result[0]['label']
            sentiment_score = classifier_result[0]['score']
            document['sentiment'] = sentiment
            document['sentiment_score'] = sentiment_score
            final_documents.append(document)
        indexer = Indexer()
        indexer.create_documents(final_documents)

if __name__ == "__main__":
    sentiment_analysis = SentimentAnalysis()
    sentiment_analysis.perform_sentiment_analysis()