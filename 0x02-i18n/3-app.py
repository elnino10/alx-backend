#!/usr/bin/env python3
""" 3 app module """

from flask import Flask, request, render_template
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """get locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def home():
    """Home route"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
