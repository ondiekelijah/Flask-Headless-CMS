from flask import request, jsonify


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
