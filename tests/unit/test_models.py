from cms.studio.models import Articles,Authors,Category

def test_new_category(client,init_database):
    """
    GIVEN a Category model
    WHEN a new category is created
    THEN check that the title field is defined correctly
    """
    category = Category(title='Tours and Travel')
    assert category.title == 'Tours and Travel'

def test_new_author(client,init_database):
    """
    GIVEN the Author model
    WHEN a new author is created
    THEN check that the name field is defined correctly
    """
    author = Authors(name='Ondiek Elijah Ochieng')
    assert author.name == 'Ondiek Elijah Ochieng'



def test_new_article(client,init_database):
    """
    GIVEN an Article model
    WHEN a new article is created
    THEN check the title,body,author_id and category_id fields are defined correctly
    """
    article = Articles(title='Importance of Testing',
     body='Flask is awesome,a non tested app is a broken application',
     author_id=1,
     category_id=1
     )

    assert article.title == 'Importance of Testing'
    assert article.body == 'Flask is awesome,a non tested app is a broken application'
    assert article.author_id == 1
    assert article.category_id == 1


