class Server:
    def __init__(self, name="No name"):
        self.name = name
        self.CUSTOMERS = {
            "thong@gmail.com": {
                "phone": "1111111111",
                "full_name": "Vo Quang Nhan 1",
            },
            "tinh@gmail.com": {
                "phone": "2222222222",
                "full_name": "Vo Quang Nhan 2",
            },
            "nhan@gmail.com": {
                "phone": "333333333",
                "full_name": "Vo Quang Nhan 3",
            },
        }

    def get_full_name(self, email):
        if self.CUSTOMERS.get(email):
           return self.CUSTOMERS[email]["full_name"]
        return "Email does not exist"

if __name__ == "__main__":
    server = Server("Mock Server")
    full_name = server.get_full_name("thong@gmail.com")
    print(full_name)
    