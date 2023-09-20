from flask_login import FlaskLoginClient
# from flask_wtf.csrf import CSRFProtect
import pytest
import bcrypt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../application")))
from compound_interest import app, db
from compound_interest.models import User, load_user
from compound_interest.routes import calculate_compound_interest

app.test_client_class = FlaskLoginClient
# csrf = CSRFProtect(app)
# csrf.init_app(app, enable=False)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SESSION_PROTECTION'] = None
    app.config['WTF_CSRF_ENABLED'] = False
    if len(list(db.users.find())) != 0:
        user_data = db.users.find_one()
        user = User(
                username=user_data["username"],
                email=user_data["email"],
                password=user_data["password"]
                )
        client = app.test_client(user=user)
    else:
        client = app.test_client()
    yield client

def login(client, username, password):
    return client.post('/login/', data = {'username': username, 'password': password})

def register(client, username, email, password):
    return client.post('/register/', data={'username': username, 'email': email, 'password1': password, 'password2': password})
    
def add_user():
    password = "password123"
    hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())  
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": hashed_pw
    }
    return db.users.insert_one(user_data)

def delete_user():
    db.users.drop()

def add_investment():
    investment = {
            "username": "testuser",
            "initial_deposit": 1000,
            "monthly_deposit": 100,
            "yearly_interest": 5,
            "years_of_investment": 10,
            "total_deposit": 13000.0,
            "total_interest": 4412.19,
            "total_money": 17412.19
        }
    db.investments.insert_one(investment)

def delete_investment():
    db.investments.drop()


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Jonathan and Binyamin Compound Interest Website' in response.data
    response = client.get('/home/')
    assert response.status_code == 200
    assert b'Welcome to Jonathan and Binyamin Compound Interest Website' in response.data


def test_register_page(client):
    response = client.get('/register/')
    assert response.status_code == 200
    assert b'Register Page' in response.data

    register_response = register(client, "testuser", "test@example.com", "password123")
    load_user("testuser")
    assert b'Username already exists! Please try a different username' not in register_response.data
    assert b'Email Address already exists! Please try a different email address' not in register_response.data
    assert response.status_code == 200

    add_user()
    register_response = register(client, "testuser", "test@example.com", "password123")
    assert b'Username already exists! Please try a different username' in register_response.data
    assert b'Email Address already exists! Please try a different email address' in register_response.data
    delete_user()


def test_login_page(client):
    response = client.get('/login/')
    assert b'Please Login' in response.data
    assert response.status_code == 200

    add_user()
    login_response = login(client, "testuser", "password123")
    assert b'Username does not exists!' not in login_response.data
    assert b'Username and password do not match. Please try again.' not in login_response.data
    assert login_response.status_code == 302 #Redirect to investments_page
    delete_user()

    login_response = login(client, "testuser", "password123")
    assert b'Username does not exists!' in login_response.data    
    

def test_logout_page(client):
    add_user()
    login(client, 'testuser', 'password123')
    response = client.get('/logout/')
    assert response.status_code == 302 #redirect
    assert response.headers['Location'] == 'http://localhost/home/'
    delete_user()


def test_investments_page(client):
    add_user()
    login(client, 'testuser', 'password123')
    
    add_investment()
    response = client.get('/investments/')
    assert response.status_code == 200
    assert b'1000' and b'100' and b'5' and b'10' in response.data

    delete_user()


def test_add_investment_page(client):
    add_user()
    login_response = login(client, 'testuser', 'password123')
    print(login_response.status_code)
    print(login_response.data)
    response = client.get('/add_investment/')
    assert response.status_code == 200
    assert b'Please Enter Your New Investment' in response.data

    delete_user()



# def test_add_investment(client, login):
#     login('testuser', 'password')
#     response = client.post('/add_investment/', data={
#         'initial_deposit': 1000,
#         'monthly_deposit': 100,
#         'yearly_interest': 5,
#         'years_of_investment': 10
#     }, follow_redirects=True)
#     assert b'Investment added successfully.' in response.data


# def test_delete_investment(client, login):
#     login('testuser', 'password')
#     # Assuming you have an investment to delete, get its ID
#     investment_id = get_investment_id_for_deletion()  # Define this function

#     response = client.post('/investments/', data={'investment_id': investment_id}, follow_redirects=True)
#     assert b'Investment deleted successfully.' in response.data


if __name__ == '__main__':
    pytest.main()