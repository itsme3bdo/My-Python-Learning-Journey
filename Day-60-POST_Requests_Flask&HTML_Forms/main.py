from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login",methods=["POST"])
def recieved_data():
    if request.method == 'POST':
        return f"<h1> Name: {request.form['username']}, Password: {request.form['password']}</h1>"
    else:
        error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
