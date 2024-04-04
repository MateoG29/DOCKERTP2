# test_app.py

from app import app as flask_app

def test_home():
    response = flask_app.test_client().get('/')
    assert response.status_code == 200
    assert "ELVIN!" in response.data.decode()
