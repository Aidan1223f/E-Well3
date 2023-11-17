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
        elif ("argument" or "arguments" or "fight" or "fights" or "fighting" or "fighting" or "arguing") in str:
            return "relationships"
        elif ("money" or "financial" or "finance" or "cash") in str:
             return "finacial" 
        elif ("grades" or "tests" or "assignments" or "homework" or "school") in str:
             return "schoolwork" 
        elif ("future" or "college" or "graduate" or "major") in str:
             return "post_highschool"
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
     
resources = {  
     "schoolwork" : "https://www.library.ca.gov/services/to-libraries/online-tutoring/#:~:text=The%20California%20State%20Library%20provides,using%20state%20curriculum%20and%20standards.",
     "relationships": "https://www.loveisrespect.org/", 
     "post_highschool" : "https://docs.google.com/presentation/d/1Pt9l4nZq33fVjyYw_Uk4BEzBvR--wWk-WjxQ9_Ta55g/edit#slide=id.p",
     "parental_argument" : "",
     "finacial" : "",
     "divorce" : "grades test",
}

resource_name = {
      "schoolwork": "California State Library Free tutoring program",
      "relationships" : "Love is Respect: relationship counseling",
      "post_highschool" : "University of California resources"
}
res_img = {
      "schoolwork" : 'hw.jpg',
      "relationships" : 'loveisrespect.jpg',
      "post_highschool" : 'uc.jpg',
     
}

time_res = {
      "this week" : "Take some time to think about this situation, there is no rush to opening up about it yet. However, when you are ready you should reach out to close friends and families for assistance",
     "1-4 weeks" : "You might want to try talking to trusted friends and family soon. They can offer their own perspective and guidance to help you get through this",
     "over 1 month" : "try talk to trusted friends and family about this issues. speaking with others is a sign of strength and they would be more than happy to help you",
}

