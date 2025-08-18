#!/usr/bin/env python3
"""Flask+Babel: forzar locale por ?locale=xx y mock de login por ?login_as=<id>."""
from flask import Flask, render_template, request, g
from flask_babel import Babel

class Config:
    """Ajustes i18n."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Mock “tabla” de usuarios
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()

def get_user():
    """Devuelve el usuario según ?login_as=<id> o None."""
    uid = request.args.get("login_as")
    try:
        return users.get(int(uid)) if uid is not None else None
    except ValueError:
        return None

@app.before_request
def before_request():
    """Guarda el user en g.user si existe."""
    g.user = get_user()

def get_locale():
    """Usa ?locale=xx si es válido; si no, Accept-Language."""
    forced = request.args.get("locale")
    if forced in app.config["LANGUAGES"]:
        return forced
    return request.accept_languages.best_match(app.config["LANGUAGES"])

babel.init_app(app, locale_selector=get_locale)

@app.route("/")
def index():
    return render_template("5-index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
