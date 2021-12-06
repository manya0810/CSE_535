#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:04:38 2019

@author: ansh
"""

import nltk
import numpy as np
from numpy.linalg import svd, norm
from collections import defaultdict, Counter
from nltk.stem.snowball import EnglishStemmer, SpanishStemmer
import detectlanguage
import pandas as pd
import os

nltk.download('perluniprops')
nltk.download('nonbreaking_prefixes')
nltk.download('punkt')
from nltk.tokenize.toktok import ToktokTokenizer

from app.backend.solr_connection import SolrConnection


class LSI:
    def __repr__(self):
        return 'LSI( terms:{}, documents:{}, index_ready:{})'.format(self.index.__len__(),
                                                                     self.documents.__len__(),
                                                                     not (self.__update_index))

    def __init__(self, tokenizer=nltk.word_tokenize,
                 english_stemmer=EnglishStemmer,
                 spanish_stemmer=SpanishStemmer,
                 english_stopwords=nltk.corpus.stopwords.words('english'),
                 spanish_stopwords=nltk.corpus.stopwords.words('spanish'),
                 variance=0.9):
        '''
        # >>> queries cannot work unless __update_index is false.
        '''
        self.english_stemmer = english_stemmer()
        self.spanish_stemmer = spanish_stemmer()
        self.tokenizer = tokenizer
        self.spanish_tokenizer = ToktokTokenizer()
        self.english_stopwords = english_stopwords
        self.spanish_stopwords = spanish_stopwords
        self.hindi_stopwords = ["मैं", "मुझको", "मेरा", "अपने आप को", "हमने", "हमारा", "अपना", "हम", "आप", "आपका",
                                "तुम्हारा", "अपने आप", "स्वयं", "वह", "इसे", "उसके", "खुद को", "कि वह", "उसकी", "उसका",
                                "खुद ही", "यह", "इसके", "उन्होने", "अपने", "क्या", "जो", "किसे", "किसको", "कि", "ये",
                                "हूँ", "होता है", "रहे", "थी", "थे", "होना", "गया", "किया जा रहा है", "किया है", "है",
                                "पडा", "होने", "करना", "करता है", "किया", "रही", "एक", "लेकिन", "अगर", "या", "क्यूंकि",
                                "जैसा", "जब तक", "जबकि", "की", "पर", "द्वारा", "के लिए", "साथ", "के बारे में", "खिलाफ",
                                "बीच", "में", "के माध्यम से", "दौरान", "से पहले", "के बाद", "ऊपर", "नीचे", "को", "से",
                                "तक", "से नीचे", "करने में", "निकल", "बंद", "से अधिक", "तहत", "दुबारा", "आगे", "फिर",
                                "एक बार", "यहाँ", "वहाँ", "कब", "कहाँ", "क्यों", "कैसे", "सारे", "किसी", "दोनो",
                                "प्रत्येक", "ज्यादा", "अधिकांश", "अन्य", "में कुछ", "ऐसा", "में कोई", "मात्र", "खुद",
                                "समान", "इसलिए", "बहुत", "सकता", "जायेंगे", "जरा", "चाहिए", "अभी", "और", "कर दिया",
                                "रखें", "का", "हैं", "इस", "होता", "करने", "ने", "बनी", "तो", "ही", "हो", "इसका", "था",
                                "हुआ", "वाले", "बाद", "लिए", "सकते", "इसमें", "दो", "वे", "करते", "कहा", "वर्ग", "कई",
                                "करें", "होती", "अपनी", "उनके", "यदि", "हुई", "जा", "कहते", "जब", "होते", "कोई", "हुए",
                                "व", "जैसे", "सभी", "करता", "उनकी", "तरह", "उस", "आदि", "इसकी", "उनका", "इसी", "पे",
                                "तथा", "भी", "परंतु", "इन", "कम", "दूर", "पूरे", "गये", "तुम", "मै", "यहां", "हुये",
                                "कभी", "अथवा", "गयी", "प्रति", "जाता", "इन्हें", "गई", "अब", "जिसमें", "लिया", "बड़ा",
                                "जाती", "तब", "उसे", "जाते", "लेकर", "बड़े", "दूसरे", "जाने", "बाहर", "स्थान",
                                "उन्हें ", "गए", "ऐसे", "जिससे", "समय", "दोनों", "किए", "रहती", "इनके", "इनका", "इनकी",
                                "सकती", "आज", "कल", "जिन्हें", "जिन्हों", "तिन्हें", "तिन्हों", "किन्हों", "किन्हें",
                                "इत्यादि", "इन्हों", "उन्हों", "बिलकुल", "निहायत", "इन्हीं", "उन्हीं", "जितना", "दूसरा",
                                "कितना", "साबुत", "वग़ैरह", "कौनसा", "लिये", "दिया", "जिसे", "तिसे", "काफ़ी", "पहले",
                                "बाला", "मानो", "अंदर", "भीतर", "पूरा", "सारा", "उनको", "वहीं", "जहाँ", "जीधर", "﻿के",
                                "एवं", "कुछ", "कुल", "रहा", "जिस", "जिन", "तिस", "तिन", "कौन", "किस", "संग", "यही",
                                "बही", "उसी", "मगर", "कर", "मे", "एस", "उन", "सो", "अत"]

        self.documents = {}
        self.index = defaultdict(Counter)
        self.solr_connection = SolrConnection()

        self.A = None  # term document matrix
        self.U = None  # output of svd
        self.S = None  # output of svd
        self.V = None  # output of svd

        self.term_rep = np.array(None)  # reduced representation of terms after svd
        self.doc_rep = np.array(None)  # reduced representation of documents after svd

        self.__update_index = True
        self._term_index_in_A = {}
        self._document_index_in_A = {}

        self.k = None  # reduced dimension after SVD
        self.variance = variance  # variance to retain after SVD

    def add_doc(self, tweet, tweet_id, language):
        '''
        add terms into vocabulary.
        add document 
        '''
        if tweet_id in self.documents:
            print('document_id : {} already indexed.'.format(tweet_id))
            return False

        if self.english_stemmer and (language == "en"):
            for token in [t.lower() for t in self.tokenizer(tweet) if t.isalpha()]:
                if token in self.english_stopwords:
                    continue
                if self.english_stemmer and (language == "en"):
                    token = self.english_stemmer.stem(token)
                    self.index[token].update({tweet_id: 1})

        if self.spanish_stemmer and (language == "es"):
            for token in [t.lower() for t in self.spanish_tokenizer.tokenize(text=tweet, return_str=True) if
                          t.isalpha()]:
                if token in self.english_stopwords:
                    continue
                if self.spanish_stemmer and (language == "es"):
                    token = self.spanish_stemmer.stem(token)
                    self.index[token].update({tweet_id: 1})
        if language == "hi":
            for token in [t.lower() for t in tweet.split(" ") if t.isalpha()]:
                if token in self.hindi_stopwords:
                    continue
                else:
                    self.index[token].update({tweet_id: 1})

        self.__update_index = True  # update flag to rebuild index
        self.documents[tweet_id] = tweet  # add document to documents
        return True

    def _svd_A(self):
        '''
        Perform SVD on A and update the U,S,V matrices
        '''
        self.U, self.S, self.V = svd(self.A)

    def _get_k_for_svd(self):
        '''
        Finds the value for k after SVD such that specified variance is retained
        returns k : int
        '''
        if (self.S is not None):
            sum = 0
            k = 0
            while (sum < self.variance):
                k -= - 1
                sum = self.S[:k].sum() / self.S.sum()
            self.k = k
            return True
        else:
            print('S is not populated.')
            return False

    def rebuild_index(self):
        '''
        # >>> set _update_index to false when index is built
        '''
        terms = list(self.index.keys())
        documents = list(self.documents.keys())
        self.A = np.zeros((terms.__len__(), documents.__len__()), dtype='uint8')

        self._document_index_in_A = {doc: ix for ix, doc in enumerate(documents)}
        self._term_index_in_A = {term: ix for ix, term in enumerate(terms)}

        for term in terms:
            counter = self.index[term]
            term_ix = self._term_index_in_A[term]
            doc_ids = list(self.index[term].keys())
            doc_vals = [counter[x] for x in doc_ids]
            doc_ixs = [self._document_index_in_A[x] for x in doc_ids]
            for ix, doc_id in enumerate(doc_ixs):
                self.A[term_ix][doc_id] = doc_vals[ix]
        print('Term-Document frequency matrix is ready.')
        print('Proceeding to do SVD on the matrix.')

        self._svd_A()
        self._get_k_for_svd()

        self.doc_rep = self.V[:self.k, :]
        self.term_rep = self.U[:, :self.k]

        print('Index Rebuilt. Setting __update_index to False. Queries can now be performed.')
        self.__update_index = False

    def _calc_query_doc_affinity_score(self, query_vector):
        '''
        calculates the query - document affinity score
        '''
        try:
            one_by_query_vector_norm_ = (1 / norm(query_vector))
        except ZeroDivisionError:
            one_by_query_vector_norm_ = (1 / 1e-4)
        affinity_scores = (np.dot(query_vector, self.doc_rep) / norm(self.doc_rep, axis=0)) * one_by_query_vector_norm_
        return affinity_scores

    def query(self, query_string, top=50):
        detectlanguage.configuration.api_key = "fdd1ebaafd1a457433d6fca7e3d6bcde"
        language = detectlanguage.simple_detect(query_string)
        if (self.__update_index == True):
            print('Index is not updated. Use rebuild_index()')
            return False

        query_vector = []
        for token in [t.lower() for t in self.tokenizer(query_string) if t.isalpha()]:
            if (token in self.english_stopwords) or (token in self.spanish_stopwords):
                continue
            if (self.english_stemmer) and language == "en":
                token = self.english_stemmer.stem(token)
            if (self.spanish_stemmer) and language == "es":
                token = self.spanish_stemmer.stem(token)
            try:
                query_vector.append(self.term_rep[self._term_index_in_A[token], :])
            except KeyError:
                query_vector.append(np.array([0.0] * self.k))

        query_vector_mean = np.array(query_vector).mean(axis=0)
        affinity_scores = self._calc_query_doc_affinity_score(query_vector_mean)

        res_doc_index = (-affinity_scores).argsort()[:top]
        results = {}
        for index in res_doc_index:
            res_doc_id = list(self._document_index_in_A.keys())[index]
            results[res_doc_id] = self.documents[res_doc_id]

        return results

    def query_execution(self, query):
        response_solr = self.solr_connection.convert_query(query)
        for tweet in response_solr:
            self.add_doc(tweet["tweet_text"], tweet["id"], tweet["tweet_lang"])
        self.rebuild_index()
        response = self.query(query)
        response_json = []
        for i in response:
            for response in response_solr:
                if i == response["id"]:
                    response_json.append(response)
                    break
        return response_json

