import requests

class MoMoServer:
    __url = "https://611ba6e422020a00175a460d.mockapi.io/momo"

    def get_amount(self, username, password):
        list_user = requests.get(self.__url).json()
        for user in list_user:
            if username == user["username"] and password == user["password"]:
                return user["amount"]
        return 0


if __name__ == "__main__":
    server = MoMoServer()
    username = "username 1"
    password = "password 1"
    amount = server.get_amount(username, password)
    print(amount)
