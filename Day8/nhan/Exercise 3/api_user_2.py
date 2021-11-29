from api import API

class APIUser2(API):
    def __init__(self):
        super().__init__()
        self.endpoint = "users-2"
    
    def get_all(self):
        list_user_temp = super().get_all()
        list_user = []
        for user in list_user_temp:
            list_user.append({
                "name" : f'{user["firstname"]} {user["lastname"]}',
                "age" : user["user_age"],
            })
        return list_user

    