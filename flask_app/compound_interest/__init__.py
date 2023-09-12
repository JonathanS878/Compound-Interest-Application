from flask import Flask
from pymongo import MongoClient
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import sys, os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SHt@dLer8j7d8z3s2023' 


# To run flask-app in containerized env use:
db_url = os.environ.get("DB_URL")
user_name = os.environ.get("USER_NAME")
password = os.environ.get("USER_PWD")
if db_url is None or user_name is None or password is None:
    print("ERROR: DB_URL, USER_NAME, and USER_PWD environment variables are not set.")
    sys.exit(1)
client = MongoClient(db_url, username=user_name, password=password)


# To run flask-app localy use:
# client = MongoClient("mongodb://localhost:27017")


db = client["ProjectDB"]
users = db["users"]
investments = db["investments"]


bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from compound_interest import routes