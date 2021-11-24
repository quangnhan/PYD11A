import uuid
from tiki_user import TikiUser

tiki = TikiUser()
response = tiki.get_all()

data = {"name": "Nathan", "job": "Developer"}
response = tiki.create(data)
print(response)
