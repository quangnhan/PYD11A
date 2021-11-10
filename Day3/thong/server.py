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
        for key in self.__CUSTOMERS:
            all_customer.append(self.__CUSTOMERS[key]["full_name"])
        return all_customer

    def get_customer_info(self, email):
        all_info = []
        if self.__CUSTOMERS.get(email):
            return self.__CUSTOMERS[email]
        return "User not exist"

    def set_customer(self, email, full_name, phone):
        self.__CUSTOMERS[email] = {"phone": phone, "full_name": full_name}
        return self.__CUSTOMERS


if __name__ == "__main__":
    server = Server("Mock Server")
    full_name = server.get_full_name("thong@gmail.com")
    print(full_name)
    all_customer = server.get_all_customer()
    print(all_customer)
    all_info = server.get_customer_info("thong@gmail.com")
    print(all_info)
    set_customer = server.set_customer("guest@gmail.com", "Mister Guest", "44444444")
    print(set_customer)
