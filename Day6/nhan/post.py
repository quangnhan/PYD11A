import requests
import uuid

url = "https://619b8723278276001744566f.mockapi.io/users"
data = {
    "id": uuid.uuid1(),
    "name": "Nhan",
    "job": "Developer"
}

response = requests.post(url, data=data)
data = response.json()

print(data)
