from datetime import datetime


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
        self.__log = list()

    # def get_full_name(self, email):
    #     for contact in self.CUSTOMERS:
    #         # print(contact, email)
    #         if contact == email:
    #             return contact[1]["full_name"]
    #             print("full_name: ", contact[1]["full_name"])

    def get_full_name(self, email):
        self.__set_log(f"{email} get name at {str(datetime.now())}")

        if self.__CUSTOMERS.get(email):
            return self.__CUSTOMERS[email]["full_name"]
        return "Email not exists"

    def get_all_customer(self):
        all_customer = []
        for key in self.__CUSTOMERS:
            all_customer.append(self.__CUSTOMERS[key]["full_name"])
        return all_customer

    def get_customer_info(self, email):
        self.__set_log(f"{email} get a customer info at {str(datetime.now())}")

        all_info = []
        if self.__CUSTOMERS.get(email):
            return self.__CUSTOMERS[email]
        return "User not exist"

    def set_customer(self, email, full_name, phone):
        self.__set_log(f"{email} set new customer at {str(datetime.now())}")

        self.__CUSTOMERS[email] = {"phone": phone, "full_name": full_name}
        return self.__CUSTOMERS

    def __set_log(self, message):
        self.__log.append(message)

    def get_log(self):
        for log in self.__log:
            print(log)


if __name__ == "__main__":
    server = Server("Mock Server")
    full_name = server.get_full_name("thong@gmail.com")
    print("thong@gmail.com: ", full_name)
    all_customer = server.get_all_customer()
    print(all_customer)
    all_info = server.get_customer_info("thong@gmail.com")
    print(all_info)
    set_customer = server.set_customer("guest@gmail.com", "Mister Guest", "44444444")
    print(set_customer)

    server.get_log()
