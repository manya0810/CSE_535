import os
import pysolr
import requests


CORE_NAME = "VSM_Project_4"
AWS_IP = "ec2-52-72-185-101.compute-1.amazonaws.com"


def delete_core(core=CORE_NAME):
    print(os.system('sudo su - solr -c "/opt/solr/bin/solr delete -c {core}"'.format(core=core)))


def create_core(core=CORE_NAME):
    print(os.system(
        'sudo su - solr -c "/opt/solr/bin/solr create -c {core} -n data_driven_schema_configs"'.format(
            core=core)))


class Indexer_VSM:
    def __init__(self):
        self.solr_url = f'http://{AWS_IP}:8983/solr/'
        self.connection = pysolr.Solr(self.solr_url + CORE_NAME, always_commit="true", timeout=500000)

    def do_initial_setup(self):
        delete_core()
        create_core()

    def create_documents(self, docs):
        print(self.connection.add(docs))

    def add_fields(self):
        '''
        Define all the fields that are to be indexed in the core. Refer to the project doc for more details
        :return:
        '''
        data = {
            "add-field":[
                {
                    "name": "poi_name",
                    "type": "string",
                    "multiValued": "false"
                },
                {
                    "name": "tweet_text",
                    "type": "text_general",
                    "multiValued": "false"
                },
                {
                    "name": "poi_id",
                    "type": "plong",
                    "multiValued": "false"
                }, {
                    "name": "verified",
                    "type": "boolean",
                    "multiValued": "false"
                },
                {
                    "name": "country",
                    "type": "string",
                    "multiValued": "false"
                },
                {
                    "name": "replied_to_tweet_id",
                    "type": "plong",
                    "multiValued": "false"
                },
                {
                    "name": "replied_to_user_id",
                    "type": "plong",
                    "multiValued": "false"
                },
                {
                    "name": "reply_text",
                    "type": "text_general",
                    "multiValued": "false"
                },
                {
                    "name": "tweet_en",
                    "type": "text_general",
                    "multiValued": "false"
                },
                {
                    "name": "tweet_es",
                    "type": "text_general",
                    "multiValued": "false"
                },
                {
                    "name": "tweet_hi",
                    "type": "text_general",
                    "multiValued": "false"
                },
                {
                    "name": "tweet_lang",
                    "type": "string",
                    "multiValued": "false"
                },
                {
                    "name": "text_en",
                    "type": "text_en",
                    "multiValued": "false"
                },{
                    "name": "text_hi",
                    "type": "text_hi",
                    "multiValued": "false"
                },{
                    "name": "text_es",
                    "type": "text_es",
                    "multiValued": "false"
                },
                {
                    "name": "hashtags",
                    "type": "strings",
                    "multiValued": "true"
                },
                {
                    "name": "mentions",
                    "type": "strings",
                    "multiValued": "true"
                },
                {
                    "name": "tweet_urls",
                    "type": "strings",
                    "multiValued": "true"
                },
                {
                    "name": "tweet_emoticons",
                    "type": "strings",
                    "multiValued": "true"
                },
                {
                    "name": "tweet_date",
                    "type": "pdate",
                    "multiValued": "false"
                },
                {
                    "name": "geolocation",
                    "type": "strings",
                    "multiValued": "true"
                }
            ],
            "replace-field-type": [
                {
                    'name': 'text_en',
                    'class': 'solr.TextField',
                    'positionIncrementGap': '100',
                    'indexAnalyzer': {
                        'tokenizer': {
                            'class': 'solr.StandardTokenizerFactory'
                        },
                        'filters': [{
                            'class': 'solr.StopFilterFactory',
                            'words': 'lang/stopwords_en.txt',
                            'ignoreCase': 'true'
                        }, {
                            'class': 'solr.LowerCaseFilterFactory'
                        }, {
                            'class': 'solr.EnglishPossessiveFilterFactory'
                        }, {
                            'class': 'solr.KeywordMarkerFilterFactory',
                            'protected': 'protwords.txt'
                        }, {
                            'class': 'solr.PorterStemFilterFactory'
                        }]
                    },
                    'similarity': {
                        'class': 'solr.ClassicSimilarityFactory'
                    },
                    'queryAnalyzer': {
                        'tokenizer': {
                            'class': 'solr.StandardTokenizerFactory'
                        },
                        'filters': [{
                            'class': 'solr.SynonymGraphFilterFactory',
                            'expand': 'true',
                            'ignoreCase': 'true',
                            'synonyms': 'synonyms.txt'
                        }, {
                            'class': 'solr.StopFilterFactory',
                            'words': 'lang/stopwords_en.txt',
                            'ignoreCase': 'true'
                        }, {
                            'class': 'solr.LowerCaseFilterFactory'
                        }, {
                            'class': 'solr.EnglishPossessiveFilterFactory'
                        }, {
                            'class': 'solr.KeywordMarkerFilterFactory',
                            'protected': 'protwords.txt'
                        }, {
                            'class': 'solr.PorterStemFilterFactory'
                        }]
                    }
                }, {
                    'name': 'text_hi',
                    'class': 'solr.TextField',
                    'positionIncrementGap': '100',
                    'indexAnalyzer': {
                        'tokenizer': {
                            'class': 'solr.WhitespaceTokenizerFactory'
                        },
                        'filters': [{
                            'class': 'solr.LowerCaseFilterFactory'
                        },
                            # {
                            #     'class': 'solr.HindiNormalizationFilterFactory'
                            # },
                            {
                                'class': 'solr.HindiStemFilterFactory'
                            }
                            # , {
                            #     'class': 'solr.SynonymFilterFactory',
                            #     'synonyms': 'hindi/synonyms.txt',
                            #     'enablePositionIncrements': 'true',
                            #     'expand': 'true'
                            # }
                        ]
                    },
                    'similarity': {
                        'class': 'solr.ClassicSimilarityFactory'
                    },
                    'queryAnalyzer': {
                        'tokenizer': {
                            'class': 'solr.WhitespaceTokenizerFactory'
                        },
                        'filters': [{
                            'class': 'solr.LowerCaseFilterFactory'
                        }, {
                            'class': 'solr.HindiStemFilterFactory'
                        },
                            # {
                            #     'class': 'HindiNormalizationFilterFactory'
                            # }
                        ]
                    }
                }, {
                    'name': 'text_es',
                    'class': 'solr.TextField',
                    'positionIncrementGap': '100',
                    'analyzer': {
                        'tokenizer': {
                            'class': 'solr.StandardTokenizerFactory'
                        },
                        'filters': [{
                            'class': 'solr.LowerCaseFilterFactory'
                        }, {
                            'class': 'solr.SpanishLightStemFilterFactory'
                        }]
                    },
                    'similarity': {
                        'class': 'solr.ClassicSimilarityFactory'
                    }
                }
            ]
        }
        print(requests.post(self.solr_url + CORE_NAME + "/schema", json=data).json())


if __name__ == "__main__":
    i = Indexer_VSM()
    i.do_initial_setup()
    i.add_fields()
