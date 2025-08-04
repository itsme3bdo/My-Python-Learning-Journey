from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    info = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7")
    dataa = info.json()
    return render_template("index.html",info=dataa)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:num>')
def get_blog(num):
    info = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7")
    dataa = info.json()
    return render_template("post.html",info=dataa,numm=num)

if __name__ == "__main__":
    app.run(debug=True)
