from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/prossesing',methods=["post"])
def prossesing():
    print request.form["name"]
    return render_template("prossesing.html")

app.run(debug=True)