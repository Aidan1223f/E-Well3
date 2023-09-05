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

# name = input("Hello, my name is Codi, what is your name? ")
# age = input("Hi " + name + ", How old are you? ")
# p1 = Person(name, age)

situation = input("How could I be of assistance? Please give me a 3-5 sentence explanation of your current situation so I can get a better understanding. ")
processed_situation = pre_processing(situation)

sentiment_analysis(processed_situation)

# print(processed_situation)
