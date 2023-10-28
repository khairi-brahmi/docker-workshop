import app
import pytest

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, Docker!" in response.data

def test_hello_invalid_route(client):
    response = client.get('/invalid_route')
    assert response.status_code == 404