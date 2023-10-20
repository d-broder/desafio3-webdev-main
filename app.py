from flask import Flask, render_template, request

import funcoes

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def sum_digits():
    if request.method == "POST":
        number = request.form["number"]
        return render_template("index.html", result=funcoes.soma_algoritmos(number))
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
