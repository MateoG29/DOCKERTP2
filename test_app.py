# test_app.py

from app import app as flask_app

def test_home():
    response = flask_app.test_client().get('/')
    assert response.status_code == 200
    assert "DevOps-TP2" in response.data.decode()
