import uuid
from tiki import Tiki
from datetime import datetime

class TikiUser(Tiki):
    def __init__(self):
        super().__init__()
        self.endpoint = "users"
    
    def create(self, data):
        data["code"] = uuid.uuid1()
        data["created_at"] = datetime.now()
        return super().create(data)

    