from api_user import APIUser
from api_user_2 import APIUser2
from api_user_3 import APIUser3
from database import Database
from datetime import datetime

dict_user = {
    "<18": {
        "min": 0,
        "max": 17,
        "count": 0,
    },
    "18-35": {
        "min": 18,
        "max": 35,
        "count": 0,
    },
    "36-60": {
        "min": 36,
        "max": 60,
        "count": 0,
    },
    ">60": {
        "min": 61,
        "max": 1000,
        "count": 0,
    },
}
def count(user):
    for key, value in dict_user.items():
        if user["age"] > value["min"] and user["age"] < value["max"]:
            dict_user[key]["count"] += 1

db = Database()
api_user = APIUser()
api_user_2 = APIUser2()
api_user_3 = APIUser3()

# API
start = datetime.now()
list_user = api_user.get_all()
list_user_2 = api_user_2.get_all()
list_user_3 = api_user_3.get_all()

for user in list_user + list_user_2 + list_user_3:
    count(user)
end = datetime.now()
print(f"Api end with: {end - start}")

# Database
start = datetime.now()
list_user_db = db.get_all_user()
for user in list_user_db:
    new_user = {
        "name": user[1],
        "age": int(user[2]),
    }
    count(new_user)
end = datetime.now()
print(f"DB end with: {end - start}")