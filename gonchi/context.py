import os
import pendulum
from markupsafe import Markup
from datetime import datetime
from flask import current_app, request

from .extensions import pages


# Context processors
def init_context_processors(app):
    @app.context_processor
    def blog_vars():
        return {
            "get_latest_blog_pages": get_latest_blog_pages,
            "publish_date": publish_date,
            "default_author": app.config["GONCHI_DEFAULT_AUTHOR"],
            "title": app.config["GONCHI_DEFAULT_TITLE"],
        }

    @app.template_filter("typography")
    def typography(s: str):
        parts = s.rsplit(" ", 1)
        if len(parts) < 2:
            return s
        return Markup("&nbsp;".join(parts))


def publish_date(page):
    t = page.meta.get("published", None)
    if t is None:
        return ""
    p = pendulum.from_format(t, "YYYY-MM-DD")
    return p.format("MMM Do, YYYY")


def get_articles():
    articles_path = os.path.join(current_app.config["FLATPAGES_ROOT"], "blog")
    articles = [
        pages.get(f"blog/{os.path.splitext(filename)[0]}")
        for filename in os.listdir(articles_path)
    ]
    articles = [
        page
        for page in articles
        if page.meta.get("title") and page.meta.get("published")
    ]
    articles = sorted(articles, key=publish_date)
    return articles


def get_latest_blog_pages(count=3):
    articles = get_articles()[:count]
    return [a for a in articles]
