from pymongo import MongoClient
import pytest


client = MongoClient("mongodb://jonathan:shtadler@localhost:27017")
db = client["ProjectDB"]



def test_data_inserted_to_mongodb():
    username = db.users.find_one({"username": "testuser"})["username"]
    assert username == "testuser"
    assert len(list(db.users.find({}))) == 1



def test_data_deletion_from_mongodb():
    db.users.delete_one({"username": "testuser"})
    assert len(list(db.users.find({}))) == 0



if __name__ == '__main__':
    pytest.main()