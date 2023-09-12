import pytest
from flask_app.compound_interest import load_user, User, calculate_compound_interest

# Define test cases for the load_user function
def test_load_user_existing_user(monkeypatch):
    # Mock the database query to return user data
    mock_db_find_one = lambda username: {"username": username, "email": "test@example.com", "password": "hashed_password"}
    
    # Replace the db.users.find_one function with the mock
    with monkeypatch.context() as m:
        m.setattr('db.users.find_one', mock_db_find_one)

        # Test with an existing user
        user = load_user("test_user")
        assert user is not None
        assert user.username == "test_user"
        assert user.email == "test@example.com"

def test_load_user_non_existing_user(monkeypatch):
    # Mock the database query to return None for non-existing user
    mock_db_find_one = lambda username: None
    
    # Replace the db.users.find_one function with the mock
    with monkeypatch.context() as m:
        m.setattr('db.users.find_one', mock_db_find_one)

        # Test with a non-existing user
        user = load_user("non_existing_user")
        assert user is None

# Define test cases for the calculate_compound_interest function
def test_calculate_compound_interest():
    # Test with example values
    initial_deposit = 1000
    monthly_deposit = 100
    yearly_interest = 5
    years_of_investment = 10

    total_deposit, total_interest, total_money = calculate_compound_interest(
        initial_deposit, monthly_deposit, yearly_interest, years_of_investment
    )

    # Assert the expected results
    assert total_deposit == 13000
    assert total_interest == 6557.92
    assert total_money == 19557.92

def test_user_class():
    # Create a user instance
    user = User(username="test_user", email="test@example.com", password="hashed_password")

    # Check if user attributes are set correctly
    assert user.username == "test_user"
    assert user.email == "test@example.com"
    assert user.password == "hashed_password"

    # Test the get_id method
    assert user.get_id() == "test_user"

    # Test the verifypw method
    assert user.verifypw("correct_password") is True
    assert user.verifypw("wrong_password") is False