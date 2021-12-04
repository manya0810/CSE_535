# -*- coding: utf-8 -*-

from googletrans import Translator
import wikipediaapi
import json
# if you are using python 3, you should
import urllib.request


# import urllib2

class SolrConnection:
    def convert_query(self, query):
        translator = Translator()
        detect = translator.detect(query)
        if detect.lang == 'en':
            text_en = query
            text_en = text_en.replace(" ", "%20")
            query = "tweet_text%3A(" + text_en + ")%0A"
            text_es = translator.translate(query, dest='es')
            text_es = text_es.text
            text_es = text_es.replace(" ", "%20")
            query = query + "tweet_text%3A(" + text_es + ")%0A"
            text_hi = translator.translate(query, dest='hi')
            text_hi = text_hi.text
            text_hi = text_hi.replace(" ", "%20")
            query = query + "tweet_text%3A(" + text_hi + ")"
        elif detect.lang == 'es':
            text_es = query
            text_es = text_es.replace(" ", "%20")
            query = "tweet_text%3A(" + text_es + ")%0A"
            text_en = translator.translate(query, dest='en')
            text_en = text_en.text
            text_en = text_en.replace(" ", "%20")
            query = query + "tweet_text%3A(" + text_en + ")%0A"
            text_hi = translator.translate(query, dest='hi')
            text_hi = text_hi.text
            text_hi = text_hi.replace(" ", "%20")
            query = query + "tweet_text%3A(" + text_hi + ")"
        else:
            text_hi = query
            text_hi = text_hi.replace(" ", "%20")
            query = "tweet_text%3A(" + text_hi + ")%0A"
            text_en = translator.translate(query, dest='en')
            text_en = text_en.text
            text_en = text_en.replace(" ", "%20")
            query = query + "tweet_text%3A(" + text_en + ")%0A"
            text_es = translator.translate(query, dest='es')
            text_es = text_es.text
            text_es = text_es.replace(" ", "%20")
            query = query + "tweet_text%3A(" + text_es + ")"
        solr_query = "http://ec2-52-72-185-101.compute-1.amazonaws.com:8983/solr/BM25_Project_4/select?q.op=OR&q=" + query + "&rows=50"
        data = urllib.request.urlopen(solr_query)
        return json.load(data)['response']['docs']

    def wiki(self, query):
        wiki = wikipediaapi.Wikipedia()
        page_py = wiki.page(query)
        if page_py.exists():

            text = page_py.summary[0:6000]
            return text
        else:
            return None
