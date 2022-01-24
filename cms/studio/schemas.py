from .main import ma


# Generate marshmallow Schemas from your models
class ArticlesShema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","title", "body", "date")


article_schema = ArticlesShema()
articles_schema = ArticlesShema(many=True)