import os
import json

# file_path = f"{os.getcwd()}/Day5/data.json"
# f = open(file_path)

# list_data = f.read()
# list_data = json.loads(list_data)

# for data in list_data:
#     print(data)

new_list_data = [
    {"id": 1, "name": "thong"},
    {"id": 2, "name": "ducnhan"},
    {"id": 3, "name": "nathan"},
]

new_file = f"{os.getcwd()}/Day5/thong/new_data.json"

f = open(new_file, "w")
json.dump(new_list_data, f)