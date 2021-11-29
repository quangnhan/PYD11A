from api_user import APIUser
from api_user_2 import APIUser2
from api_user_3 import APIUser3
from database import Database

# user = {"name" : "Nhan Vo", "age" : "26"}

db = Database()
api_user = APIUser()
api_user_2 = APIUser2()
api_user_3 = APIUser3()

# Get data
list_user = api_user.get_all()
list_user_2 = api_user_2.get_all()
list_user_3 = api_user_3.get_all()

# Inserdata
id = 1
for user in list_user + list_user_2 + list_user_3:
    user["id"] = id
    db.insert_user(user)
    id += 1