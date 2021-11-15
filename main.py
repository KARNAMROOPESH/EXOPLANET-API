from flask import Flask,jsonify,request
from data import data

app = Flask(__name__)

@app.route("/")

def index():
    return  jsonify({
        "planetdata":data
    })

@app.route("/planet")
def planet():
    planetname = request.args.get("name")
    planetdata = 0
    for i in data:
        if i["name"] == planetname:
            planetdata = i
            break
    return jsonify({
        "planet":planetdata
    })


if __name__ == "__main__":
    app.run(debug = True)
