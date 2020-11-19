import numpy as np
import pandas as pd
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

import pickle


tokenizer = pickle.load(open('tokenizer.pkl','rb+'))

model = load_model('model.h5')



def input(name):
    q = tokenizer.texts_to_sequences(name)
    q = [i[0] for i in q]
    q1 = []
    q1.append(q)
    s = pad_sequences(q1,maxlen=80,padding='post')
    return s

def decoder(ans):
    decode = np.argmax(ans,axis=1)[0]
    return decode

def get_gender(name):
    name = name.lower()
    labels = {1:'male',0:'female','nada':'undefined'}
    result = name
    if name!='nada':
        sequences = input(name)
        predict = model.predict(sequences)
        result = decoder(predict)
    #print('{}, is a {}'.format(name,labels[result]))
    return labels[result]
    




