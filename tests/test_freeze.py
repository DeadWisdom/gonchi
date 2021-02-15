import gonchi
from example.app import app, freeze


def test_freeze():
    freeze(app)
