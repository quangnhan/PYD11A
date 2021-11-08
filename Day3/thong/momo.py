class Momo:
    def __init__(self, name):
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

    def hello_full_name(self, email):
        if self.CUSTOMERS.get(email):
            print("Hello there ", self.CUSTOMERS[email]["full_name"])
        else:
            print("Email not exists")


if __name__ == "__main__":
    server = Momo("Mock Momo")
    full_name = server.hello_full_name("thong@gmail.com")
    # print(full_name)