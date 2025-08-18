#!/usr/bin/env python3
"""Flask+Babel: locale (URL > user > header > default) y timezone (URL > user > UTC)."""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    """Ajustes i18n."""
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
    """User por ?login_as=<id> o None."""
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
    """Prioridad: ?locale -> user.locale -> Accept-Language -> default."""
    param = request.args.get("locale")
    if param in app.config["LANGUAGES"]:
        return param
    user = getattr(g, "user", None)
    if user and user.get("locale") in app.config["LANGUAGES"]:
        return user["locale"]
    best = request.accept_languages.best_match(app.config["LANGUAGES"])
    return best or app.config["BABEL_DEFAULT_LOCALE"]


@babel.timezoneselector
def get_timezone():
    """Prioridad: ?timezone -> user.timezone (válidos) -> 'UTC'."""
    tz = request.args.get("timezone")
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass
    user = getattr(g, "user", None)
    if user:
        utz = user.get("timezone")
        if utz:
            try:
                pytz.timezone(utz)
                return utz
            except UnknownTimeZoneError:
                pass
    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/")
def index():
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
