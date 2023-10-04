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
# app.config['SQLALCHEMY_DATABASE_URL'] = 'sqllite///db.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class User(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(50))
  
logic = {1: "Hello! My name is Codi. What is your name?",
         2: "How could I be of assistance? Please give me a 3-5 sentence explanation of your current situation so I can get a better understanding.",
         3: "TEST",
         }
log_i = 1
person = {
  

}


@app.route('/', methods=["POST", "GET"])
def index():
  content = logic[log_i + 1]
  if request.method == "POST":
    message = request.form["message"]
    message = pre_processing(message)

    user = request.form["name"]
    age = request.form["age"]

    person = {"user": user, "age": age, "message": message}
    print(person)
    return render_template('questionare.html', content=content)
  else:
    return render_template('index.html', content=content)

@app.route("/login", methods=["POST", "GET"])
def log():
  if request.method == "POST":
    #request from the form in login.html
    user = request.form["nm"]
    session["user"] = user
    #redirects to a url "user" displaying the user's name
    return redirect(url_for("user"))
  else:
    if "user" in session:
      return render_template('login.html')


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

@app.route("/questionare", methods=["POST", "GET"])
def questionare():
  if request.method == "POST":
    log_i += 1
    quest = logic[log_i]

    ans = request.form[ans]
  return ans


if __name__ == "__main__":
  app.run(debug=True, port=8001) 
