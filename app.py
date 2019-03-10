from functools import wraps
import re

from flask import Flask
from flask import render_template, request
from flask_csp.csp import csp_header
from spellchecker import SpellChecker

app = Flask(__name__)
spell = SpellChecker(distance=1)

alpha_re = re.compile("[A-Za-z]+")


def parse_tokens(message):
    tokens = message.split(" ")
    tokens = {i for i in tokens if alpha_re.match(i)}
    return tokens


@app.route("/", methods=["GET", "POST"])
@csp_header(
    {
        "default-src": "'self'",
        "style-src": "'self' *.bootstrapcdn.com",
        "script-src": "'self' cdnjs.cloudflare.com *.bootstrapcdn.com code.jquery.com",
    }
)
def index():
    if request.method == "POST":
        if "message" not in request.form:
            render_template("index.html")

        msg = request.form["message"]
        tokens = parse_tokens(msg)
        mispelled = spell.unknown(tokens)
        corrections = {word: spell.correction(word) for word in mispelled}
        return render_template("index.html", corrections=corrections, message=msg)

    return render_template("index.html", message=None)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
