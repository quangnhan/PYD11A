from api import API
from database import Database

api = API()
db = Database()

# Get data
list_user = api.get_all_user()

# Save data
for user in list_user:
    db.insert_user(user)