from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hotels")
def hotels():
    return render_template("hotels.html")

@app.route("/details")
def details():
    return render_template("details.html")

@app.route("/booking", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        checkin = request.form.get("checkin")
        checkout = request.form.get("checkout")
        return render_template("confirmation.html", name=name)

    

    return render_template("booking.html")


if __name__ == "__main__":
    app.run(debug=True)