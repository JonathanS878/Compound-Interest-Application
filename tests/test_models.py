import pytest
import bcrypt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../application")))
from compound_interest.models import User, calculate_compound_interest
from compound_interest import db



def test_calculate_compound_interest():
    initial_deposit = 1000
    monthly_deposit = 100
    yearly_interest = 5
    years_of_investment = 10
    total_deposit, total_interest, total_money = calculate_compound_interest(
        initial_deposit, monthly_deposit, yearly_interest, years_of_investment
    )
    assert total_deposit == 13000
    assert total_interest == 4412.19
    assert total_money == 17412.19

def test_user_class():
    password = "password123"
    hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    user = User(username="testuser", email="test@example.com", password=hashed_pw)

    # check if user attributes are set correctly
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.password == hashed_pw

    # test the get_id method
    assert user.get_id() == "testuser"

    # test the verifypw method
    user_data = {
        "username": user.username,
        "email": user.email,
        "password": user.password
    }
    db.users.insert_one(user_data)
    assert user.verifypw("password123") is True
    assert user.verifypw("wrong_password") is False

    db.users.drop()


if __name__ == '__main__':
    pytest.main()