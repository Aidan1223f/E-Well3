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
        elif ("money" or "financial" or "finance" or "cash") in str:
             return "finacial" 
        elif ("grades" or "tests" or "assignments" or "homework") in str:
             return "schoolwork" 
        else:
            print('Can you be a little more specific?')

resp = {
    
     "divorce" : "I'm really sorry to hear that you're feeling this way, and I want you to know that you're not alone. It's completely normal to face challenges in school, and it's okay to ask for help. You have a lot of potential, and I believe in your ability to overcome this. Together, we can work on finding solutions that will make things better for you. Remember, progress is a journey, and I'm here to support you every step of the way.",
     "parental_argument" : "",
     "finacial" : "",
     "schoolwork" : "grade test 2",
    }

def response(str):
     if ("divorce") in str:
          return resp["divorce"]
     if ("parental_argument"):
          return resp["parental_argument"]
     if ("finacial") in str:
          return resp["finacial"]
     if("schoolwork") in str:
          return resp["schoolwork"]
     
resources = {  "divorce" : "https://www.library.ca.gov/services/to-libraries/online-tutoring/#:~:text=The%20California%20State%20Library%20provides,using%20state%20curriculum%20and%20standards.",
     "parental_argument" : "",
     "finacial" : "",
     "schoolwork" : "grades test",
}

resource_name = {
      "schoolwork": "California State Library Free tutoring program",
}
res_img = {
      "divorce" : "src/brainfuse-gethomeworkhelp@600.jpg",
     "parental_argument" : "",
     "finacial" : "",
     "schoolwork" : "src/brainfuse-gethomeworkhelp@600.jpg",
}

yes = {
      "divorce" : "try talk to trusted friends and family about this issues. speaking with others is a sign of strength and they would be more than happy to help you",
     "parental_argument" : "",
     "finacial" : "",
     "schoolwork" : "try talk to trusted friends and family about this issues. speaking with others is a sign of strength and they would be more than happy to help you",
}

def link_resource(str):
     if ("divorce") in str:
          return resources["divorce"]
     if ("parental_argument"):
          return resources["parental_argument"]
     if ("finacial") in str:
          return resources["finacial"]
     if("schoolwork") in str:
          return resources["schoolwork"]