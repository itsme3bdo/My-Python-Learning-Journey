from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, Email
from flask_bootstrap import Bootstrap5
from flask import Flask

app = Flask(__name__)


class MyForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(message='Please enter a valid email address with an @ and a .')])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label="Log In")


bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    form = MyForm(meta={'csrf':False})
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
