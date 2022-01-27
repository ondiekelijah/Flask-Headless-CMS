# Create a test client using the Flask application configured for testing
import pytest,requests,json
from cms.studio.app import create_app


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            yield client

