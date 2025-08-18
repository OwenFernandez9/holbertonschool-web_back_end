#!/usr/bin/env python3
"""Flask+Babel i18n con override por ?locale=xx"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Ajustes i18n para Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel()


def get_locale():
    """Usa ?locale=xx si es válido; si no, Accept-Language."""
    forced = request.args.get("locale")
    if forced in app.config["LANGUAGES"]:
        return forced
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Home localizada."""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
