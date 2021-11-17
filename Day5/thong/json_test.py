import os
import json

file_path = f"{os.getcwd()}/Day5/data.json"
f = open(file_path)

list_data = f.read()
list_data = json.loads(list_data)

for data in list_data:
    print(data)