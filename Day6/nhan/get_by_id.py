import requests

url = "https://619b8723278276001744566f.mockapi.io/users"
id = 1
response = requests.get(f"{url}/{id}")
data = response.json()

print(data)
