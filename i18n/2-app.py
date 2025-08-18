#!/usr/bin/env python3
"""
Flask app + Babel with locale selection from Accept-Language
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration for Flask-Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()

def get_locale():
    """
    Pick the best match between the client's Accept-Language header
    and the languages supported by our app.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])

babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render index page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
