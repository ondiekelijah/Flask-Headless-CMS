from flask import request, jsonify
import pytest,requests,app,json
from main import app

# Create a test client using the Flask application configured for testing

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_fetch_articles(client) :

    path = "api/articles"
    response = client.get(path)
    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200


def test_fetch_article(client) :

    path = "api/articles/1"
    response = client.get(path)
    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200
