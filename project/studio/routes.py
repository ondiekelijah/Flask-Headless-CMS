from flask import Blueprint
from .forms import ArticleForm,AuthorForm,CategoryForm
from .uploader import upload_img
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

from werkzeug.routing import BuildError
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)

from models import Articles,articles_schema,Category,Authors

studio = Blueprint("studio", __name__, url_prefix="/studio")

# Fetch authors and categories from the database


# CLIENT STUDIO ROUTES
# ARTICLES

def get_authors():
    authors_list = Authors.query.with_entities(Authors.name).all()
    return authors_list

    
def get_categories():
    category_list = Category.query.with_entities(Category.title).all()
    return category_list


@studio.route("/", methods=["GET", "POST"], strict_slashes=False)
def index():
    return render_template("studio/index.html",title="Studio | Home")


@studio.route("/articles", methods=["GET"], strict_slashes=False)
def articles():

    articles = Articles.query.filter_by(id=Articles.id).order_by(Articles.date.desc()).all()

    return render_template("studio/articles.html",articles=articles,title="Studio | Articles")


@studio.route("articles/<int:article_id>",methods=["GET", "POST"],strict_slashes=False)
def article(article_id):
    
    article = Articles.query.filter_by(id=article_id).first_or_404()

    return render_template('studio/article.html',article=article,title="Studio | Article")


@studio.route("/new-article", methods=["GET", "POST"], strict_slashes=False)
def add_article():

    form = ArticleForm()

    categories = [(c.id, c.title) for c in Category.query.filter_by(id=Category.id).all()]
    authors = [(c.id, c.name) for c in Authors.query.filter_by(id=Authors.id).all()]

    form = ArticleForm(request.form)
    form.category.choices = categories
    form.author.choices = authors

    if request.method =='POST':
        try:
            picture_file = upload_img(request.files['file'])

            title = request.form.get("title")
            body = request.form.get("content")
            image = picture_file


            author = form.author.data
            category = form.category.data

            article = Articles(
                title=title,
                body=body,
                image=image,
                author_id=author,
                category_id=category

            )

            db.session.add(article)
            db.session.commit()
            flash(f"Article succesfully published", "success")

            return redirect(url_for("studio.articles"))

        except InvalidRequestError:
            db.session.rollback()
            flash(f"Something went wrong!", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"IntegrityError!.", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "warning")
        except InterfaceError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except DatabaseError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"An error occured !", "danger")

    return render_template("studio/add.html",
        form=form,
        authors_list=get_authors(),
        category_list=get_categories(),
        btn_text="Publish article",
        action="Write a new article",
        title="Studio | New article"
        )



@studio.route("/articles/update/<int:article_id>/",methods=["GET", "POST"],strict_slashes=False)
def update_article(article_id):

    form = ArticleForm()

    categories = [(c.id, c.title) for c in Category.query.filter_by(id=Category.id).all()]
    authors = [(c.id, c.name) for c in Authors.query.filter_by(id=Authors.id).all()]

    form = ArticleForm(request.form)
    form.category.choices = categories
    form.author.choices = authors

    article = Articles.query.filter_by(id=article_id).first()

    if form.validate_on_submit() and request.method =='POST':
        try:
            article.title = form.title.data
            article.body = form.body.data
            article.category_id = form.category.data
            article.author_id = form.author.data

            if form.image.data:
                picture_file = upload_img(form.image.data)
                article.image = picture_file

            db.session.commit()
            flash(f"Article succesfully updated", "success")
            return redirect(url_for("studio.articles"))

        except Exception as e:
            db.session.rollback()
            flash(e, "danger")

    elif request.method =='GET':

        form.title.data = article.title
        form.body.data = article.body
        form.author.data = article.author_id
        form.category.data = article.category_id



    return render_template("studio/add.html",
        form=form,
        btn_text="Update article",
        action="Update article",
        title="Studio | Update article"
        )




@studio.route("/articles/delete/<int:article_id>/",methods=["GET", "POST"],strict_slashes=False)
def delete_article(article_id):
    article = Articles.query.filter_by(id=article_id).first()

    db.session.delete(article)
    db.session.commit()
    flash(f"Article deleted!", "success")

    return redirect(url_for("studio.articles"))

# Article Categories

@studio.route("/categories",methods=["GET", "POST"], strict_slashes=False)
def categories():
    form = CategoryForm()

    categories = Category.query.filter_by(id=Category.id).all()

    if request.method == "POST" and form.validate_on_submit():

        try:
            title = form.c_title.data
              
            category = Category(
                title=title
            )
            db.session.add(category)
            db.session.commit()
            flash(f"Category succesfully added", "success")

            return redirect(url_for("studio.categories"))

        except Exception as e:
            db.session.rollback()
            flash(e, "danger")

    return render_template("studio/categories.html",
        form=form,
        categories=categories,
        top_btn_action="Add category",
        btn_text="Save",
        action="Manage Categories",
        title="Studio | Category"
        )


@studio.route("/category/update/<int:category_id>/",methods=["GET", "POST"],strict_slashes=False)
def update_category(category_id):

    form = CategoryForm()

    category = Category.query.filter_by(id=category_id).first()


    if form.validate_on_submit() and request.method =='POST':
        try:
            category.title = form.title.data

            db.session.commit()
            flash(f"Record succesfully updated", "success")
            return redirect(url_for("studio.categories"))

        except Exception as e:
            db.session.rollback()
            flash(e, "danger")
    elif request.method =='GET':

        form.title.data = category.title

    return render_template("studio/categories.html",
        category=category,
        form=form,
        btn_text="Save",
        top_btn_action="Update category",
        action="Update Category",
        title="Studio | Update Category"
        )




@studio.route("/categorys/delete/<int:category_id>/",methods=["GET", "POST"],strict_slashes=False)
def delete_category(category_id):
    category = Category.query.filter_by(id=category_id).first()

    db.session.delete(category)
    db.session.commit()
    flash(f"Category deleted!", "success")

    return redirect(url_for("studio.categories"))

# Authors

@studio.route("/authors", methods=["GET", "POST"], strict_slashes=False)
def authors():
    form = AuthorForm()

    if request.method == "GET":

        authors = Authors.query.filter_by(id=Authors.id).all()

    elif request.method == "POST" and form.validate_on_submit():

        try:
            name = form.name.data
              
            author = Authors(
                name=name
            )
            db.session.add(author)
            db.session.commit()
            flash(f"Author succesfully added", "success")

            return redirect(url_for("studio.authors"))

        except Exception as e:
            db.session.rollback()
            flash(e, "danger")

    return render_template("studio/authors.html",
        authors=authors,
        form=form,
        top_btn_action="Add author",
        btn_text="Save Author",
        action="Manage Authors",
        title="Studio | New Author"
        )


@studio.route("/authors/update/<int:author_id>/",methods=["GET", "POST"],strict_slashes=False)
def update_author(author_id):

    form = AuthorForm()

    author = Authors.query.filter_by(id=author_id).first()


    if form.validate_on_submit() and request.method =='POST':
        try:
            author.name = form.name.data

            db.session.commit()
            flash(f"Record succesfully updated", "success")
            return redirect(url_for("studio.authors"))

        except Exception as e:
            db.session.rollback()
            flash(e, "danger")

    elif request.method =='GET':

        form.name.data = author.name

    return render_template("studio/authors.html",
        form=form,
        author=author,
        top_btn_action="Update author",
        btn_text="Save",
        action="Update Author",
        title="Studio | Update Author"
        )




@studio.route("/authors/delete/<int:author_id>/",methods=["GET", "POST"],strict_slashes=False)
def delete_author(author_id):
    author = Authors.query.filter_by(id=author_id).first()

    db.session.delete(author)
    db.session.commit()
    flash(f"Author deleted!", "success")

    return redirect(url_for("studio.authors"))


