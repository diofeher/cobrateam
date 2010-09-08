from flask import Flask, render_template

app = Flask("CobraTeam Website")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/staff")
def staff():
    return render_template("staff.html")

@app.route("/challenges")
def challenges():
    return render_template("challenges.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
