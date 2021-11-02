from flask import Blueprint
# from .forms import *
# from . import *
from app import db
# bcrypt, login_manager
from flask import current_app

# from flask_login import (
#     UserMixin,
#     login_required,
#     login_user,
#     LoginManager,
#     current_user,
#     logout_user,
#     login_required,
# )

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

# from werkzeug.routing import BuildError
# from sqlalchemy.exc import (
#     IntegrityError,
#     DataError,
#     DatabaseError,
#     InterfaceError,
#     InvalidRequestError,
# )

from models import Articles,articles_schema

api = Blueprint("api", __name__, url_prefix="/api")


# CLIENT STUDIO ROUTES

@api.route("/articles", methods=["GET"], strict_slashes=False)
def articles():

  articles = Articles.query.all()
  results = articles_schema.dump(articles)

  return jsonify(results)