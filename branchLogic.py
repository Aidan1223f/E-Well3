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
        global problem
        if ("divorce" or "divorced") in str:
            return "divorce"
        elif ("argument" or "argument with parents" or "argument with family" or "arguing") in str:
            return"parental argument"
        elif ("money" or "financial" or "finance" or "cash"):
             return "finacial" 
        else:
            print('false')

# def followup_quest:



# print(processed_situation)
