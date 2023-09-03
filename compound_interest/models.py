from compound_interest import login_manager, bcrypt, db
from flask_login import UserMixin



@login_manager.user_loader
def load_user(_id):
    return User.objects.get(_id=_id)



class User(UserMixin):
    def __init__(self, _id, username, email, password):
        super(User, self).__init__()
        self._id = _id
        self.username = username
        self.email = email
        self.password = password

    def isuserexist(self):
        return (db.users.find({"username": self.username}).count()!=0)

    def isemailexist(self):
        return (db.users.find({"email": self.email}).count()!=0)

    def verifypw(self, password):
        hashed_pw = db.users.find({"username" : self.username})[0]["password"]
        return (bcrypt.hashpw(password.encode('utf8'), hashed_pw)==hashed_pw)



class Investment():
    def __init__(self, _id, user_id, initial_deposit, monthly_deposit, yearly_interest, years_of_investment, total_deposit, total_interest, total_money):
        super(Investment, self).__init__()
        self._id = _id
        self.user_id = user_id
        self.initial_deposit = initial_deposit
        self.monthly_deposit = monthly_deposit
        self.yearly_interest = yearly_interest
        self.years_of_investment = years_of_investment
        self.total_deposit = total_deposit
        self.total_interest = total_interest
        self.total_money = total_money



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