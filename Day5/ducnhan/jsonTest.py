import os
import json

filePath = f"{os.getcwd()}/Day5/ducnhan/data.json"
f = open(filePath)

listData = f.read()
listData = json.loads(listData)

for data in listData:
    print(data)