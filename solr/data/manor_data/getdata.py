import pickle
import pandas as pd
import json
import os

json_lst_key = [] #index for keywords
json_lst_poi = [] #index for pois

dl = os.listdir('keywords')
for f in dl:
    file = open('keywords/'+f,'rb')
    df = pickle.load(file)
    json_lst_key.extend([dict(v) for _, v in df.iterrows()])
    file.close()

dl = os.listdir('pois')
for f in dl:
    file = open('pois/'+f,'rb')
    df = pickle.load(file)
    json_lst_poi.extend([dict(v) for _, v in df.iterrows()])
    file.close()







