from datetime import datetime

class Server:
    def __init__(self, name="No name"):
        self.name = name
        self.__CUSTOMERS = {
            "thong@gmail.com": {
                "phone": "1111111111",
                "full_name": "Vo Quang Nhan 1",
                "amount": "100"
            },
            "tinh@gmail.com": {
                "phone": "2222222222",
                "full_name": "Vo Quang Nhan 2",
                "amount": "200"
            },
            "nhan@gmail.com": {
                "phone": "333333333",
                "full_name": "Vo Quang Nhan 3",
                "amount": "300"
            },
        }
        self.__log = list()

    def __set_log(self, message):
        self.__log.append(message)

    def get_log(self):
        print(self.__log)

    def get_full_name(self, email):
        self.__set_log(f"{email} get name at {str(datetime.now())}")

        if self.__CUSTOMERS.get(email):
            return self.__CUSTOMERS[email]["full_name"]
        return "Email doesn't exiest"

    def get_amount(self, email):
        self.__set_log(f"{email} get amount at {str(datetime.now())}")

        if self.__CUSTOMERS.get(email):
            return self.__CUSTOMERS[email]["amount"]
        return 0

if __name__ == "__main__":
    server = Server("Mock Server")
    full_name = server.get_full_name("thong@gmail.com")
    full_name = server.get_full_name("thong@gmail.com")
    full_name = server.get_full_name("thong@gmail.com")
    server.get_log()