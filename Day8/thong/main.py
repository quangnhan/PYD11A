from server import UserAPI, UserDatabase

# get user data from API
user_api = UserAPI()

data = user_api.get_all()

# insert data into db postgres
user_database = UserDatabase()
for item in data:
    user_database.insert(item)
data_in_db = user_database.get_all()
print(data_in_db)
