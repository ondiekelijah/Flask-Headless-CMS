from models import Articles,Authors,Category


# def test_new_user():
#     """
#     GIVEN a User model
#     WHEN a new User is created
#     THEN check the email, hashed_password, and role fields are defined correctly
#     """
#     user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
#     assert user.email == 'patkennedy79@gmail.com'
#     assert user.hashed_password != 'FlaskIsAwesome'
#     assert user.role == 'user'


def test_new_category():
    """
    GIVEN a Category model
    WHEN a new category is created
    THEN check that the title field is defined correctly
    """
    category = Category('Tests in Flask')
    assert category.title == 'Tests in Flask'

def test_new_author():
    """
    GIVEN the Author model
    WHEN a new author is created
    THEN check that the name field is defined correctly
    """
    author = Authors('John Doe')
    assert author.name == 'John Doe'



def test_new_article():
    """
    GIVEN an Article model
    WHEN a new article is created
    THEN check the title,body,author_id and category_id fields are defined correctly
    """
    article = Articles('Unit Tests in Flask',
     'FlaskIsAwesome,a non tested app is a broken application',
     1,1)

    assert article.title == 'Unit Tests in Flask'
    assert article.body != 'FlaskIsAwesome,a non tested app is a broken application'
    assert article.author_id == 1
    assert article.category_id == 1


