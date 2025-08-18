#!/usr/bin/env python3
"""Flask+Babel: prioridad de locale URL > user > header > default."""
from flask import Flask, render_template, request, g
from flask_babel import Babel

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

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
    uid = request.args.get("login_as")
    try:
        return users.get(int(uid)) if uid is not None else None
    except ValueError:
        return None

@app.before_request
def before_request():
    g.user = get_user()

def get_locale():
    """Prioridad: ?locale -> g.user.locale -> Accept-Language -> default."""
    param = request.args.get("locale")
    if param in app.config["LANGUAGES"]:
        return param
    user = getattr(g, "user", None)
    if user and user.get("locale") in app.config["LANGUAGES"]:
        return user["locale"]
    best = request.accept_languages.best_match(app.config["LANGUAGES"])
    return best or app.config["BABEL_DEFAULT_LOCALE"]

babel.init_app(app, locale_selector=get_locale)

@app.route("/")
def index():
    return render_template("5-index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
