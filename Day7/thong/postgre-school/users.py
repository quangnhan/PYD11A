from server import Server


class UsersManager(Server):
    def __init__(self):
        super().__init__()
        self.table = "users"
