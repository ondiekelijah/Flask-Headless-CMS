from flask import Blueprint
from ..studio.main import db
from flask import current_app

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    abort,
    current_app,
    jsonify
)

from ..studio.models import Articles
from ..studio.schemas import article_schema,articles_schema

api = Blueprint("api", __name__, url_prefix="/api")


# CLIENT STUDIO ROUTES

@api.route("/articles", methods=["GET"], strict_slashes=False)
def articles():

  articles = Articles.query.all()
  results = articles_schema.dump(articles)

  return jsonify(results)

@api.route("/articles/<int:article_id>/",methods=("GET", "POST"),strict_slashes=False)
def article(article_id):
    article = Articles.query.filter_by(id=article_id).first()
    return article_schema.dump(article)