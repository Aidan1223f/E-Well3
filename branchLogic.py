import nltk
import numpy as np
import re 
import string
from nltk.corpus import stopwords


nltk.download('stopwords')

def pre_processing(wrds):
    wrds = wrds.lower()
    wrds = re.sub('[%s]' % re.escape(string.punctuation), '', wrds)

    stop_words = set(stopwords.words('english'))
    wrds = " ".join([word for word in wrds.split() if word not in stop_words])
    wrds = wrds.split()
    
    return wrds

def sentiment_analysis(str):
        if ("divorce" or "argument") in str:
            print('true')
        else:
            print('false')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# print(processed_situation)
