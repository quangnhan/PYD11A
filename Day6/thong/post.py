import requests

url = "https://619b87292782760017445671.mockapi.io/users"
data = {"name": "Tran Quoc Thong", "job": "Full-Stack Web Developer"}

response = requests.post(url, data=data)
print(data)