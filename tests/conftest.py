# Create a test client using the Flask application configured for testing
import pytest,requests,json
from cms.studio.app import create_app
from cms.studio.main import db
from cms.studio.models import Articles,Authors,Category
import config

@pytest.fixture
def client():
    app = create_app()
    app.config.from_object('config.TestingConfig')
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture()
def init_database():
    # Create the database and the database table
    db.create_all()
 
    # Insert test data
    category = Category(title='Tests in Flask')
    author = Authors(name='Ondiek Elijah')
    article = Articles(title='Unit Tests in Flask',
     body='FlaskIsAwesome,a non tested app is a broken application',
     author_id=1,
     category_id=1
     )

    db.session.add(category)
    db.session.add(author)
    db.session.add(article)

    # Commit the changes for the users
    db.session.commit()
 
    yield db  # this is where the testing happens!
    db.session.remove()  # looks like db.session.close() would work as well
    db.drop_all()
