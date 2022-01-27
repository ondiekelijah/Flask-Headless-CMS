from cms.studio.models import Articles,Authors,Category

def test_new_category():
    """
    GIVEN a Category model
    WHEN a new category is created
    THEN check that the title field is defined correctly
    """
    category = Category(title='Tests in Flask')
    assert category.title == 'Tests in Flask'

def test_new_author():
    """
    GIVEN the Author model
    WHEN a new author is created
    THEN check that the name field is defined correctly
    """
    author = Authors(name='John Doe')
    assert author.name == 'John Doe'



def test_new_article():
    """
    GIVEN an Article model
    WHEN a new article is created
    THEN check the title,body,author_id and category_id fields are defined correctly
    """
    article = Articles(title='Unit Tests in Flask',
     body='FlaskIsAwesome,a non tested app is a broken application',
     author_id=1,
     category_id=1
     )

    assert article.title == 'Unit Tests in Flask'
    assert article.body == 'FlaskIsAwesome,a non tested app is a broken application'
    assert article.author_id == 1
    assert article.category_id == 1


