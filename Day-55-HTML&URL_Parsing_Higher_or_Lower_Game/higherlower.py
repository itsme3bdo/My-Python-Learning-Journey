#parsing is knowing what the user typed in the url
from random import randint,choice
from flask import Flask


def heading(function):
    def wrapper():
        return "<h1>"+function()+"</h1>"
    return wrapper

app = Flask(__name__)



@app.route('/')
def hello_world():
    return ('<h1 style="color:blue;">Guess a number between 0 and 9</h1>'
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExamZtMjB2azJiOWZzMDBqeDExOWJ5YzRlcTlydWJvamdqbTNwcWNwcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/z1HdiobjzYIrm/giphy.gif" width=400>')
howa = randint(0,9)

@app.route(f"/{howa}")
def say_bye():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    color = choice(colors)
    return (f"<h1 style='color:{color};'>You found me!</h1>"
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmhrcjM3bWlxdHpncDBjZ2RoY2ppM3pydjU1NDh2dmg0aWtpZXBwbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BPJmthQ3YRwD6QqcVD/giphy.gif' width=400>")

@app.route('/<int:num>')
def show_user_profile(num):
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    # show the user profile for that user
    if num > howa:
        color = choice(colors)
        return (f'<h1 style="color:{color};">Too high, try again!</h1>'
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWI0bmR3MXU1a3BuNmhsYmloYmx1Zzh0bjJjZ24wMmVocXRjNWEydyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Wn8mIfu3syxqD25d1A/giphy.gif" width=400>')
    else:
        color = choice(colors)
        return (f'<h1 style="color:{color};">Too low, try again!</h1>'
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDN3amtnZ3FnNnU3N2ptd2QwOHNhMjBtMTgydnVvYjlvMXN0cWxyMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ta3v3I4GI1gH7Rqek6/giphy.gif" width=400>')


if __name__ == "__main__":
    app.run()
