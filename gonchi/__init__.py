from flask import Flask, render_template
from flask_frozen import Freezer
from .base import Gonchi, pages


def freeze(app):
    f = Freezer(app)
    f.freeze()
    return f