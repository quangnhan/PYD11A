from server import Server

class Momo:
    def __init__(self, email):
        self.server = Server()
        self.email = email
        self.full_name = self.server.get_full_name(email)

    def get_amount(self):
        return self.server.get_amount(self.email)

if __name__ == "__main__":
    momo = Momo("nhan@gmail.com")
    amount = momo.get_amount()
    print(amount)
    


