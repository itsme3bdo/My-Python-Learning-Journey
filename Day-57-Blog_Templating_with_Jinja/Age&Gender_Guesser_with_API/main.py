import random
from flask import Flask, render_template
from random import randint
from datetime import date
from future.backports.datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number=random.randint(1,10)
    current_year = datetime.today().year
    return render_template("index.html",num=random_number,year=current_year)


@app.route(f'/guess/<username>')
def hello_world(username):
    now = date.today().year
    response = requests.get(url=f"https://api.agify.io/?name={username}")
    data1 = response.json()
    agee = data1["age"]
    response2=requests.get(url=f"https://api.genderize.io/?name={username}")
    data2 = response2.json()
    genderr=data2["gender"]
    return render_template('guess.html',name=username.title(),datee=now,gender=genderr,age=agee)

@app.route('/blog/<num>')
def get_blog(num):
    info = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    dataa = info.json()
    return render_template("blog.html",inn=dataa)


if __name__ == "__main__":
    app.run(debug=True)
