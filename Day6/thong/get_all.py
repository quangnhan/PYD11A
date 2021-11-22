import requests

url = "https://619b87292782760017445671.mockapi.io/users"

response = requests.get(url)

data = response.json()
print(data)
