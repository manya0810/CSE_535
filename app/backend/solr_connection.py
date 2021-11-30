# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should
import urllib.request

# import urllib2

class SolrConnection:
    def convert_query(self, query):
        query = query.replace(" ", "%20")
        query = "tweet_text%3A" + query
        solr_query = "http://ec2-52-72-185-101.compute-1.amazonaws.com:8983/solr/BM25_Project_4/select?q.op=OR&q=" + query + "&rows=50"
        data = urllib.request.urlopen(solr_query)
        return json.load(data)['response']['docs']

