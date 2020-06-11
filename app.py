from domain.identity import user
from flask import Flask
from flask import jsonify
app = Flask(__name__)

#brlja

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/html")
def html():
    return "<html><head></head><body><h1>Hello Flask!</h1></body></html>"

@app.route("/json/<fname>/<lname>")
def json(fname, lname):
    u = user.User(fname, lname)
    return jsonify(u.__dict__)