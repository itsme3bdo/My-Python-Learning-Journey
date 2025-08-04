from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    info = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    dataa = info.json()

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    info = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    dataa = info.json()
    return render_template("index.html",inn=dataa)

@app.route('/post/<int:num>')
def get_blog(num):
    info = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    dataa = info.json()
    return render_template("post.html",inn=dataa,numm=num)

if __name__ == "__main__":
    app.run(debug=True)

    return render_template("index.html",inn=dataa)

@app.route('/post/<int:num>')
def get_blog(num):
    info = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    dataa = info.json()
    return render_template("post.html",inn=dataa,numm=num)

if __name__ == "__main__":
    app.run(debug=True)
