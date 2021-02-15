from gonchi import Flask, Gonchi, freeze

GONCHI_DEFAULT_AUTHOR = "Gonchi Test"
GONCHI_DEFAULT_TITLE = "Gonchi Example"

app = Flask(__name__)
app.config.from_object(__name__)
gonchi = Gonchi(app)

if __name__ == "__main__":
    freeze(app)
