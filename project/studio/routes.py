from flask import Blueprint
from .forms import ArticleForm
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

from models import Articles,articles_schema

studio = Blueprint("studio", __name__, url_prefix="/studio")


# CLIENT STUDIO ROUTES
@studio.route("/", methods=["GET", "POST"], strict_slashes=False)
def index():
    return render_template("studio/index.html")


@studio.route("/articles", methods=["GET"], strict_slashes=False)
def articles():

    articles = Articles.query.filter_by(id=Articles.id).all()

    return render_template("studio/articles.html",articles=articles)


@studio.route("articles/<int:post_id>",methods=["GET", "POST"],strict_slashes=False)
def article(post_id):
    
    article = Post.query.filter_by(id=post_id).first_or_404()

    return render_template('studio/article.html',article=article)


@studio.route("/new-article", methods=["GET", "POST"], strict_slashes=False)
def add_article():

    form = ArticleForm()
    if form.validate_on_submit():
        try:
            title = form.title.data
            body = form.body.data

                
            article = Articles(
                title=title,
                body=body
            )
            db.session.add(article)
            db.session.commit()
            flash(f"Article succesfully published", "success")

            return redirect(url_for("studio.articles"))

        except Exception as e:
            db.session.rollback()
            flash(e, "danger")

    return render_template("studio/add.html",form=form,btn_text="Publish article")


@studio.route("/articles/update/<int:article_id>/",methods=["GET", "POST"],strict_slashes=False)
def update_article(article_id):

    form = ArticleForm()

    article = Articles.query.filter_by(id=article_id).first()


    if form.validate_on_submit() and request.method =='POST':
        try:
            article.title = form.title.data
            article.body = form.body.data

            db.session.commit()
            flash(f"Article succesfully updated", "success")

        except Exception as e:
            db.session.rollback()
            flash(e, "danger")
    elif request.method =='GET':

        form.title.data = article.title
        form.body.data = article.body


    return render_template("studio/add.html",form=form,btn_text="Update article")




@studio.route("/articles/delete/<int:article_id>/",methods=["GET", "POST"],strict_slashes=False)
def delete_article(article_id):
    article = Articles.query.filter_by(id=article_id).first()

    db.session.delete(article)
    db.session.commit()
    flash(f"Article deleted!", "success")

    return redirect(url_for("studio.articles"))
