import pytest
from flask_app.compound_interest import app 
from flask_webtest import TestApp

# Create a TestApp instance to interact with your app
test_app = TestApp(app)


def test_home_page():
    response = test_app.get('/')
    assert response.status_code == 200
    assert "Welcome to the Home Page" in response.text


def test_investments_page():
    response = test_app.get('/investments/')
    assert response.status_code == 200
    assert "Investments" in response.text


def test_add_investment_page():
    response = test_app.get('/add_investment/')
    assert response.status_code == 200
    assert "Add Investment" in response.text


def test_register_page():
    response = test_app.get('/register/')
    assert response.status_code == 200
    assert "Register" in response.text


def test_login_page():
    response = test_app.get('/login/')
    assert response.status_code == 200
    assert "Login" in response.text


def test_logout_page():
    response = test_app.get('/logout/')
    assert response.status_code == 302  # Check if it redirects after logout