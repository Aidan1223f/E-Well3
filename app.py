from flask import Flask, flash, render_template, session, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import nltk
import numpy as np
import re 
import string
from nltk.corpus import stopwords
nltk.download('stopwords')

from branchLogic import sentiment_analysis, pre_processing

app = Flask(__name__)
app.secret_key = "bello"

  
logic = {1: "Hello! My name is Codi. What is your name?",
         2: "How could I be of assistance? Please give me a 3-5 sentence explanation of your current situation so I can get a better understanding.",
         3: "TEST",
         }
log_i = 1
person = {
  "problem": []

}
quest ="ppp"


@app.route('/', methods=["POST", "GET"])
def index():
    global log_i
    content = logic[log_i + 1]
    if request.method == "POST":
        message = request.form["message"]
        message = pre_processing(message)

        user = request.form["name"]
        age = request.form["age"]

        person = {"user": user, "age": age, "message": message, "problem" : sentiment_analysis(message)}
        print(person)
        return redirect(url_for("questionare", quest=logic[3]))
    else:
        return render_template('index.html', content=content)

@app.route("/questionare", methods=["GET", "POST"])
def questionare():
    if request.method == "POST":
        log_i += 1
        ans = request.form["ans"]
        print(ans)
        print(log_i)
    return render_template('questionare.html', quest=logic[3])


@app.route("/user")
def user():
  if "user" in session:
    user = session["user"]
    return f"<h1>{user}</h1>"
  else: 
    if "user" in session:
      return redirect(url_for("user"))
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
  session.pop("user", None)
  return render_template('login.html')

if __name__ == "__main__":
  app.run(debug=True, port=8001) 
