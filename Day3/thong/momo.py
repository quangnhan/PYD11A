from server import Server


class Momo:
    def __init__(self, email):
        server = Server()

        print(server)
        print(f"Server name: {server.name}")

        self.email = email
        self.full_name = server.get_full_name(email)
        print(f"Hello {self.full_name}")

        self.all_customer = server.get_all_customer()
        print(f"This is all customers: {self.all_customer}")

        self.customer_info = server.get_customer_info("tinh@gmail.com")
        print(f"This is a customer info: {self.customer_info}")

        self.new_customer = server.set_customer(
            "director@gmail.com", "The Executive Director", 999999999
        )
        print(f"This is the new customer: {self.new_customer}")

        self.activity_log = server.get_log()
        # print(f"This is log {self.activity_log}") # get_log() already print


if __name__ == "__main__":

    momo = Momo("thong@gmail.com")
