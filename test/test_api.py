import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_api_get_posts(client):
    resp = client.get("/api/post/")
    assert resp.status_code == 200
    assert type(resp.json) == list
    assert len(resp.json) > 0


def test_api_get_post(client):
    resp = client.get("/api/post/1")
    assert resp.status_code == 200
    assert type(resp.json) == dict
    assert set(resp.json.keys()) == {
        "poster_name",
        "poster_avatar",
        "pic",
        "content",
        "views_count",
        "likes_count",
        "pk"
    }
