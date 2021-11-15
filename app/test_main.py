from starlette.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello!! this is a small api which will give you dog facts."}
