from .main import db
from datetime import datetime

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    body = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(150), nullable=True)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable = False)
    author = db.relationship('Authors', backref='author',lazy=True)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable = False)
    category = db.relationship('Category', backref='category',lazy=True)



    def __repr__(self):
        return "<Articles %r>" % self.title


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300),nullable=False)


    def __repr__(self):
        return "<Authors %r>" % self.name

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300),nullable=False)


    def __repr__(self):
        return "<Category %r>" % self.title

