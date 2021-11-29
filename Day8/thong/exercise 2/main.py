from server import UserAPI, UserDatabase

# get user data from API
user_api = UserAPI()

data_1 = user_api.get_all("users")
data_2 = user_api.get_all("students")
data_3 = user_api.get_all("customers")

print(data_1)
print(data_2)
print(data_3)


# insert data into db postgres
user_database = UserDatabase()
for item in data_1:
    user_database.insert(item)

for item in data_2:
    user_database.insert(item)


data_in_db = user_database.get_all()
print(data_in_db)
