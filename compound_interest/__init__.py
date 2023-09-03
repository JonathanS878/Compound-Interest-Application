from flask import Flask
from pymongo import MongoClient
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

client = MongoClient("mongodb://db:27017")
db = client.ProjectDB
users = db["Users"]
investments = db["Investments"]

app.config['SECRET_KEY'] = 'SHt@dLer8j7d8z3s2023' 

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from compound_interest import routes



# from flask import Flask
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
# from pymongo import MongoClient

# app = Flask(__name__)
# # Connect to MongoDB
# login = LoginManager(app)
# login.login_view = 'login'





# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
# login_manager.login_view = "login_page"
# login_manager.login_message_category = "info"
# from compound_interest import routes