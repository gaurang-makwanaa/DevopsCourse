from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Replace with real Atlas URI

client = MongoClient("mongodb+srv://dummy:1234@tram.conawp2.mongodb.net/")
db = client["testdb"]
collection = db["users"]

@app.route("/", methods=["GET","POST"])
def form():
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            data = {"name": name, "email":email}
            collection.insert_one(data)

            return redirect(url_for("success"))
        
        except Exception as e:
            return render_template("form.html", error=str(e))
        
    return render_template("form.html") 

@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)