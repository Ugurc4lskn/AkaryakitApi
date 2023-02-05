from flask import Flask, jsonify, render_template
from functions import petrolOfisi, plakaKodu, türkiyePetrolleri

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/petrolofisi/<string:il>")
def allPrice(il):
    if len(petrolOfisi(il=il)) != 0:
        return jsonify({
            "data":{
                "satus":"succes",
                "price": (petrolOfisi(il=il)),
            }})

    else:
        return jsonify({
            "status":"fail"
        })


@app.route("/tppd/<string:il>")
def tppdPrice(il: str = ...):
    plakaKod = plakaKodu(il=il)
    if plakaKod != None:
        return jsonify({
            "data":{
                "status":"succes",
                "price":  türkiyePetrolleri(plakaKod=plakaKod)
            }
        })
    
    else:
        return jsonify({
            "status":"fail"
        })




if __name__ == "__main__":
    app.run(debug=True)