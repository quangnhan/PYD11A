import requests

url = "https://619b87292782760017445671.mockapi.io/users"
id = 2

response = requests.delete(f"{url}/{id}")
data = response.json()

print(data)