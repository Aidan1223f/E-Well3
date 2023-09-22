from flask import Flask, render_template, session, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import nltk
import numpy as np
import re 
import string
from nltk.corpus import stopwords

app = Flask(__name__)
app.secret_key = "bello"

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqllite///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

logic = {1: "Hello! My name is Codi. What is your name?",
         2: "How could I be of assistance? Please give me a 3-5 sentence explanation of your current situation so I can get a better understanding.",
         }

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  



@app.route('/', methods=["POST", "GET"])
def index():
  content = logic[1]
  if request.method == "POST":
    # user = request.form["name"]
    message = request.form["message"]
    return redirect(url_for("message",msg=message))
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

@app.route("/<msg>")
def message(msg):
  return f"<h1>{msg}</h1>"

def pre_processing(wrds):
    wrds = wrds.lower()
    wrds = re.sub('[%s]' % re.escape(string.punctuation), '', wrds)

    stop_words = set(stopwords.words('english'))
    wrds = " ".join([word for word in wrds.split() if word not in stop_words])
    wrds = wrds.split()
    
    return wrds



if __name__ == "__main__":
  app.run(debug=True, port=8001) 
