#parsing is knowing what the user typed in the url

from flask import Flask
def bold(function):
    def wrapper():
        return "<b>"+function()+"</b>"
    return wrapper
def italic(function):
    def wrapper():
        return "<em>"+function()+"</em>"
    return wrapper
def underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper
app = Flask(__name__)



@app.route('/')
@bold
@underline
@italic
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()
