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
import json

nltk.download('punkt')


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
        self.english_stopwords = english_stopwords
        self.spanish_stopwords = spanish_stopwords

        self.documents = {}
        self.index = defaultdict(Counter)

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

        for token in [t.lower() for t in self.tokenizer(tweet) if t.isalpha()]:
            if (token in self.english_stopwords) or (token in self.spanish_stopwords):
                continue
            if self.english_stemmer and (language == "en"):
                token = self.english_stemmer.stem(token)
            if self.spanish_stemmer and (language == "es"):
                token = self.spanish_stemmer.stem(token)

            # add this token to defaultdict(Counter)
            # this document's count is increased by 1 for this token's Counter
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

    def query(self, query_string, top=10):
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
        results = []
        for index in res_doc_index:
            res_doc_id = list(self._document_index_in_A.keys())[index]
            results.append(self.documents[res_doc_id])

        return results


if __name__ == "__main__":
    lsi = LSI()
    list_of_path = ['data/rshah_data']
        # , 'data/manor_data/keywords', 'data/manor_data/pois', 'data/manya_data']

    for path in list_of_path:
        files = os.listdir(path)
        for file in files:
            docs = pd.read_pickle(f"{path}/{file}").to_dict('records')
            for tweet in docs:
                lsi.add_doc(tweet["tweet_text"], tweet["id"], tweet["tweet_lang"])

    list_of_json_path = ['data/sachin_data/json_main', 'data/sachin_data/json_non_poi']

    # for path in list_of_json_path:
    #     files = os.listdir(path)
    #     for file in files:
    #         with open(path + "/" + file) as json_file:
    #             data = json.load(json_file)
    #             for tweet in data:
    #                 lsi.add_doc(tweet["tweet_text"], tweet["id"], tweet["tweet_lang"])
    lsi.rebuild_index()
    query = "vaccine passport"
    response = lsi.query(query)
    for i in response:
        print(i)

'''

'''
