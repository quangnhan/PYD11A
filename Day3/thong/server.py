class Server:
    def __init__(self, name="No Name Server"):
        self.name = name
        self.CUSTOMERS = {
            "thong@gmail.com": {
                "phone": "1111111111",
                "full_name": "Thong Tran",
            },
            "tinh@gmail.com": {
                "phone": "2222222222",
                "full_name": "Tong Dang Tinh",
            },
            "nhan@gmail.com": {
                "phone": "333333333",
                "full_name": "Vo Quang Nhan",
            },
        }

    # def get_full_name(self, email):
    #     for contact in self.CUSTOMERS:
    #         # print(contact, email)
    #         if contact == email:
    #             return contact[1]["full_name"]
    #             print("full_name: ", contact[1]["full_name"])

    def get_full_name(self, email):
        if self.CUSTOMERS.get(email):
            return self.CUSTOMERS[email]["full_name"]
        return "Email not exists"


if __name__ == "__main__":
    server = Server("Mock Server")
    full_name = server.get_full_name("thong@gmail.com")
    print(full_name)