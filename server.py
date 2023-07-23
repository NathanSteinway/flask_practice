from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cupcake_fav")
def fav():
    return render_template("fav.html", cupcakes = get_cupcakes("fav.csv"))

@app.route("/cupcake_all")
def all():
    return render_template("all.html", cupcakes = get_cupcakes("sample.csv"))

@app.route("/cupcake_order")
def order():
    return render_template("order.html", cupcakes = get_cupcakes("order.csv"))

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("sample.csv", name)

    if cupcake: 
        add_cupcake_dictionary("order.csv", cupcake)
        return redirect(url_for("home"))
    else:
     return "Sorry, I couldn't find one!"
    
@app.route("/add-fav/<name>")
def fav_cupcake(name):
    cupcake = find_cupcake("sample.csv", name)

    if cupcake: 
        add_cupcake_dictionary("fav.csv", cupcake)
        return redirect(url_for("home"))
    else:
     return "Sorry, I couldn't find one!"

if __name__ == "__main__":

    app.env = "development"
    app.run(
        debug=True,
        port=8000,
        host = "localhost"
    )