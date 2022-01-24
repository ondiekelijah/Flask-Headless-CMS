import os
import tempfile

import pytest

from ...cms.studio.main import app,db

# Create a test client using the Flask application configured for testing


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_page(client):

    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    
    response = client.get('/')
    assert response.status_code == 200
    assert b'Headless CMS in Flask' in response.data


