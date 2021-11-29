from api import API

class APIUser(API):
    def __init__(self):
        super().__init__()
        self.endpoint = "users"
    

    