import os
import json

# file_path = f"{os.getcwd()}/Day5/data.json"
# f = open(file_path)

# list_data = f.read()
# list_data = json.loads(list_data)

list_data = [
    {
        "id": 1,
        "name": "Name 1"
    },
    {
        "id": 2,
        "name": "Name 3"
    }
]
new_file = f"{os.getcwd()}/Day5/nhan/new_data.json"
f = open(new_file, "w")
json.dump(list_data, f)