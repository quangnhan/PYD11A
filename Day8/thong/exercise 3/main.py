from server import UserAPI

users_data = UserAPI()

data_1 = users_data.get_all()
count_18 = 0
for p in data_1:
    if p["age"] < 18:
        count_18 += 1

print(count_18)
