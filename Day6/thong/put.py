import requests

url = "https://619b87292782760017445671.mockapi.io/users"

data = {"name": "Vo Quang Nhan", "job": "Project Manager"}
id = 1
response = requests.put(f"{url}/{id}", data=data)
data = response.json()

print(data)
