from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def hello_word():
    return render_template("agenda1.html")