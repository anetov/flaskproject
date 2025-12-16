from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def blog():
    return render_template('about.html')

@app.route("/blog/2025/dog")
def blog2():
    return "<h1>My dog</h1>"