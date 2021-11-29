from api import API

class APIUser3(API):
    def __init__(self):
        super().__init__()
        self.endpoint = "users-3"

    def get_all(self):
        list_user_temp = super().get_all()
        list_user = []
        for user in list_user_temp:
            list_user.append({
                "name" : user["fullname"],
                "age" : user["age"],
            })
        return list_user
    

    