import os
from flask import Flask, render_template
from jinja2 import ChoiceLoader, PackageLoader
from .extensions import pages
from .context import init_context_processors


class Gonchi(object):
    def __init__(self, app=None, strict_slashes=False):
        self.app = app
        self.strict_slashes = strict_slashes
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("FLATPAGES_AUTO_RELOAD", True)
        app.config.setdefault("FLATPAGES_EXTENSION", ".md")
        app.config.setdefault("FLATPAGES_ROOT", os.path.join(app.root_path, "pages"))
        app.config.setdefault("FLATPAGES_MARKDOWN_EXTENSIONS", ["nl2br"])
        app.config.setdefault("FLATPAGES_MARKDOWN_CONFIG", {"nl2br": None})
        app.config.setdefault("FREEZER_REMOVE_EXTRA_FILES", True)

        # Rather these raise exceptions, actually.
        # app.config.setdefault('GONCHI_DEFAULT_AUTHOR', 'Gonchi')
        # app.config.setdefault('GONCHI_DEFAULT_TITLE', 'Gonchi')

        app.jinja_loader = ChoiceLoader(
            [
                app.jinja_loader,
                PackageLoader("gonchi"),
            ]
        )

        if self.strict_slashes is not None:
            app.url_map.strict_slashes = self.strict_slashes

        pages.init_app(app)
        init_context_processors(app)
        self.setup_routes(app)

    def setup_routes(self, app):
        # Home / Index
        @app.route("/")
        def index(path=None):
            """Home page has a different template."""
            page = pages.get_or_404("index")
            return render_template("index.html", page=page, title=page.meta["title"])

        @app.route("/blog/index.html")
        def blog(path=None):
            """Home page has a different template."""
            return render_template("blog.html", page=page, title="Blog")

        @app.route("/blog/<path:path>.html")
        def blog_item(path=None):
            page = pages.get_or_404("blog/" + path)
            return render_template(
                "blog-page.html", page=page, title=page.meta["title"]
            )

        @app.route("/<path:path>")
        def page(path=None):
            page = pages.get_or_404(path)
            return render_template("page.html", page=page, title=page.meta["title"])
