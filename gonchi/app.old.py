from flask import Flask, render_template

from extensions import pages
from context import init_context_processors

# Tell Flatpages to auto reload when a page is changed, and look for .md files
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = ".md"

# Create our app object, use this page as our settings (will pick up DEBUG)
app = Flask(__name__)

# For settings, we just use this file itself, very easy to configure
app.config.from_object(__name__)

# We want Flask to allow no slashes after paths, because they get turned into flat files
app.url_map.strict_slashes = False

# Create an instance of our extension
pages.init_app(app)

# Add context processors
init_context_processors(app)

# Home / Index
@app.route("/")
def index(path=None):
    """Home page has a different template."""
    page = pages.get_or_404("index")
    return render_template("index.html", page=page, title=page.meta["title"])


@app.route("/blog")
def blog(path=None):
    """Home page has a different template."""
    return render_template("blog.html", page=page, title="Articles")


@app.route("/articles/<path:path>")
def article(path=None):
    page = pages.get_or_404("articles/" + path)
    return render_template("article-page.html", page=page, title=page.meta["title"])


@app.route("/<path:path>")
def page(path=None):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page, title=page.meta["title"])
