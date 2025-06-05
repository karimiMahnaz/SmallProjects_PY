import pandas as pd
import numpy as np

from keras.api.models import Sequential 
from keras.api.layers import Dense
from keras.api.activations import relu
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import json
from hazm import Normalizer, WordTokenizer
# from hazm import Normalizer
# normalizer = Normalizer()
# print(normalizer.normalize("سلام    خوبی؟"))

with open('PredictLikeNo/data.json', 'r+') as f:
    print(f.name)
    data = json.load(f)
    print(data[0])

    for p in data:
        print(p['content'])
       # print(p['reactions'])
       # print(p['comments'])

        normalizer = Normalizer()
        tokenize = WordTokenizer()
    
        print('before' + p['content'])
        p['content'] = normalizer.normalize(p['content'])
        print('after' + p['content'])
        print( tokenize.tokenize(p['content']))

df = pd.DataFrame(data)

#df = df.drop(['id', 'title', 'url', 'time', 'section', 'author'], axis = 1)