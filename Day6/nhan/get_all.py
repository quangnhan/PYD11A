import requests

url = "https://619b8723278276001744566f.mockapi.io/users"
response = requests.get(url)
data = response.json()

print(data)
