class Server:
    def __init__(self, name="No Name Server"):
        self.name = name
        self.__CUSTOMERS = {
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
        if self.__CUSTOMERS.get(email):
            return self.__CUSTOMERS[email]["full_name"]
        return "Email not exists"

    def get_all_customer(self):
        all_customer = []
        for customer in self.__CUSTOMERS:
            print(customer.get("full_name"))
        #     all_customer.append(customer["full_name"])
        # return all_customer


if __name__ == "__main__":
    server = Server("Mock Server")
    full_name = server.get_full_name("thong@gmail.com")
    print(full_name)
    all_customer = server.get_all_customer()
    print(all_customer)