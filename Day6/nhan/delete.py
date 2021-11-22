import requests

url = "https://619b8723278276001744566f.mockapi.io/users"
id = 3

response = requests.delete(f"{url}/{id}")
data = response.json()

print(data)
