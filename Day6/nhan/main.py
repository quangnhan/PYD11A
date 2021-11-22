import uuid
from server import TikiAPI

tiki = TikiAPI()
data = {
    "id": uuid.uuid1(),
    "name": "Nhan",
    "job": "Developer"
}
response = tiki.create(data)

# print(uuid.uuid1())