import requests

url = "https://619b8723278276001744566f.mockapi.io/users"
id = 1
data = {
    "name": "Thong",
    "job": "Developer"
}

response = requests.put(f"{url}/{id}", data=data)
data = response.json()

print(data)
