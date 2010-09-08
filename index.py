from flask import Flask, render_template, url_for

app = Flask("CobraTeam Website")

@app.route("/")
def index():
    return render_template("index.html", hello_msg = "Dorgas Manolo")

if __name__ == "__main__":
    app.run(debug=True)
