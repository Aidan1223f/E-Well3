from flask import Flask, flash, render_template, session, url_for, redirect, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import nltk
import numpy as np
import re 
import string
from nltk.corpus import stopwords
nltk.download('stopwords')

from branchLogic import sentiment_analysis, pre_processing, response, link_resource, yes, res_img, resource_name
app = Flask(__name__)
app.secret_key = "bello"


logic = ["How long have you been feeling like this? ", "Who have you talked to about this issue?", "test"] 
        

person = {"user" : "null", "user_type" :"null", "gradelvl" : 0, "message" : "null", "problem" : "schoolwork"}

@app.route('/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"] 
        user_type = request.form["user_type"]

        person = {"user": user, "user_type" : user_type }
        print(person)
        if user_type == "Admin":
            return redirect(url_for("admin"))
        elif user_type == "Student":
            return redirect(url_for("index"))
    else:
        return render_template('login.html')

@app.route('/admin', methods=["POST", "GET"])
def admin():
    p = person
    return render_template("admin.html", person=p)

@app.route('/index', methods=["POST", "GET"])
def index():
    content =  "How could I be of assistance? Please give me a 3-5 sentence explanation of your current situation so I can get a better understanding."
    if request.method == "POST":
        message = request.form["message"]
        message = pre_processing(message)

        person = { "message": message, "problem" : sentiment_analysis(message)}
        global results
        results = "I'm really sorry to hear that you're feeling this way, and I want you to know that you're not alone. It's completely normal to face challenges in school, and it's okay to ask for help. You have a lot of potential, and I believe in your ability to overcome this. Together, we can work on finding solutions that will make things better for you. Remember, progress is a journey, and I'm here to support you every step of the way."
    
        return redirect(url_for("res", result=results))
        # return redirect(url_for("questionare", quest=logic[1]))
    else:
        return render_template('index.html', content=content)
    
results = "I'm really sorry to hear that you're feeling this way, and I want you to know that you're not alone. It's completely normal to face challenges in school, and it's okay to ask for help. You have a lot of potential, and I believe in your ability to overcome this. Together, we can work on finding solutions that will make things better for you. Remember, progress is a journey, and I'm here to support you every step of the way."
@app.route("/res", methods=["GET", "POST"])
def res():
   
    if request.method == "POST":
        return redirect(url_for("questionare", quest=logic[0]))
    else:
        return render_template("results.html", results=results)
    


resources = link_resource(person["problem"])
resource_img = res_img[person["problem"]]
final_res = yes[person["problem"]]
nm = resource_name[person["problem"]]

@app.route("/questionare", methods=["GET", "POST"])
def questionare():  
    if request.method == "POST":    
        ans1 = request.form["inputs1"]
        ans2 = request.form["inputs2"]
            
        return render_template("finalres.html",  resources=resources, img=resource_img, name=nm,fr= final_res)
    else:
        return render_template('questionare.html')



@app.route("/final_results")    
def final_results():
    return render_template("finalres.html",  resources=resources, img=resource_img, name=nm,fr= final_res)
    
if __name__ == "__main__":
    app.run(debug=True, port=5000) 
