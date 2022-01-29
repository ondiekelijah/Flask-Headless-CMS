def test_fetch_articles(client,init_database) :

    path = "api/articles"
    response = client.get(path)
    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200
    assert b"Unit Tests in Flask" in response.data
    assert b"FlaskIsAwesome,a non tested app is a broken application" in response.data


def test_fetch_article(client,init_database) :

    path = "api/articles/1"
    response = client.get(path)
    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200
    assert b"Unit Tests in Flask" in response.data
    assert b"FlaskIsAwesome,a non tested app is a broken application" in response.data

