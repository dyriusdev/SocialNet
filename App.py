from flask import Flask, render_template
import html

app : Flask = Flask(__name__)

@app.route("/")
def Index() -> str:
    return "Init flask"

@app.route("/entry")
def Entry() -> html:
    return render_template("entry.html", page_title="Test")

app.run()