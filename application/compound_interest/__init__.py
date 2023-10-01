from flask import Flask
from pymongo import MongoClient
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
secret_key = os.environ.get("SECRET_KEY")
app.config['SECRET_KEY'] = secret_key 
if secret_key is None:
    app.config['SECRET_KEY'] = "key_for_pytest_jonathan&binyamin"

hostname = os.environ.get("HOST_NAME")
username = os.environ.get("MONGO_DB_USERNAME")
password = os.environ.get("MONGO_DB_PASSWORD")
MONGO_URI = f"mongodb://{username}:{password}@{hostname}/"
if hostname is not None or username is not None or password is not None:
    client = MongoClient(MONGO_URI)
else:
    client = MongoClient("mongodb://localhost:27017")


db = client["ProjectDB"]
users = db["users"]
investments = db["investments"]


bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from compound_interest import routes