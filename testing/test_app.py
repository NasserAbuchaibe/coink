"""File containg test for app"""

import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()

# Checking successful response to main page with GET method
def test_home(client):
    resp = client.get('/')
    assert resp.status_code == 200

 # Checking successful response to /list route with get method
def test_list_bad_http_method(client):
    resp = client.get('/list')
    assert resp.status_code == 200
