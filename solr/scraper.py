'''
@author: Souvik Das
Institute: University at Buffalo
'''

import json
import pandas as pd
from indexer_bm25 import IndexerBM25
from indexer_vsm import Indexer_VSM
import os


def read_config():
    with open("config.json") as json_file:
        data = json.load(json_file)

    return data


def write_config(data):
    with open("config.json", 'w') as json_file:
        json.dump(data, json_file)


def save_file(data, filename):
    df = pd.DataFrame(data)
    df.to_pickle("data/" + filename)


def read_file(type, id):
    return pd.read_pickle(f"data/{type}_{id}.pkl")


def main():
    indexer_vsm = Indexer_VSM()
    indexer_bm25 = IndexerBM25()

    list_of_path = ['data/manya_data', 'data/manor_data/keywords', 'data/manor_data/pois', 'data/rshah_data']

    for path in list_of_path:
        files = os.listdir(path)
        for file in files:
            docs = pd.read_pickle(f"{path}/{file}").to_dict('records')
            indexer_vsm.create_documents(docs)
            indexer_bm25.create_documents(docs)

    list_of_json_path = ['data/sachin_data/json_main', 'data/sachin_data/json_non_poi']

    for path in list_of_json_path:
        files = os.listdir(path)
        for file in files:
            with open(path + "/" + file) as json_file:
                data = json.load(json_file)
                indexer_vsm.create_documents(data)
                indexer_bm25.create_documents(data)


if __name__ == "__main__":
    main()
