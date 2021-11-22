import uuid
from server import TikiAPI

tiki = TikiAPI()

data = {"name": "Nathan", "job": "Developer"}

response = tiki.create_user(data)
print(uuid.uuid1())

edit_user = tiki.edit_user(data, id)

delete_user = tiki.delete_user(id)
get_by_user_id = tiki.get_by_user_id(id)