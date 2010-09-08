from flask import Flask, render_template, url_for

app = Flask("CobraTeam Website")

@app.route("/")
def index():
    return render_template("index.html", msg = "Dorgas Manolo")

@app.route("/staff")
def staff():
    return render_template("index.html", msg = "Team")

@app.route("/challenges")
def challenges():
    return render_template("index.html", msg = "challenges")

@app.route("/contact")
def contact():
    return render_template("index.html", msg = "contact")

if __name__ == "__main__":
    app.run(debug=True)
