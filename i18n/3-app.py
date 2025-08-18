#!/usr/bin/env python3
"""
Flask app with Babel i18n, locale selection, and templated message IDs
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """Configuration for Flask-Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


def get_locale():
    """Pick best match from Accept-Language"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    # Example usage in Python (not strictly required for this task)
    _title = _("home_title")
    _header = _("home_header")
    return render_template(
        "3-index.html", page_title=_title, page_header=_header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
