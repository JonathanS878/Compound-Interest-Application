from compound_interest import login_manager, db
from flask_login import UserMixin
import bcrypt


@login_manager.user_loader
def load_user(username):
    user_data = db.users.find_one({"username": username})
    if not user_data:
        return None
    user = User(user_data["username"], user_data["email"], user_data["password"])
    return user



class User(UserMixin):
    def __init__(self, username, email, password):
        super(User, self).__init__()
        self.username = username
        self.email = email
        self.password = password

    def get_id(self):
        return str(self.username)

    def verifypw(self, password):
        hashed_pw = db.users.find_one({"username": self.username})["password"]
        return bcrypt.checkpw(password.encode('utf8'), hashed_pw)

 


def calculate_compound_interest(initial_deposit, monthly_deposit, yearly_interest, years_of_investment):    
     # Calculate the number of compounding periods per year (assuming monthly contributions)
    n = 12
        
    # Calculate the total number of compounding periods
    total_periods = years_of_investment * n
        
    total_deposit = initial_deposit
    total_money = (initial_deposit+monthly_deposit)*(1 + yearly_interest/100/n)
        
    for i in range(total_periods):
        total_deposit += monthly_deposit
        total_money += monthly_deposit
        total_money = total_money*(1 + yearly_interest/100/n)


    # Calculate the total interest by subtracting total_deposit from total_money
    total_interest = total_money - total_deposit
        
    return round(total_deposit, 2), round(total_interest, 2), round(total_money, 2)