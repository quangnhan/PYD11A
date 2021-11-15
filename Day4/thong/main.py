from momo_server import MoMoServer


class PaymentApp:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.amount = 0

    def pay(self, amount):

        self.amount = amount
        print(f"Confirm payment of {amount}.00 USD")


class Momo(MoMoServer):
    def __init__(self, username, password):
        super().__init__(username, password)
        server = MoMoServer()
        self.amount = server.get_amount(self.username, self.password)
        return f"The Momo Amount is {self.amount}"


class VNPay(PaymentApp):
    pass


class Zalo_Pay(PaymentApp):
    pass


momo = Momo("username 2", "password 2")
momo_amount = momo.get_amount("username 2", "password 2")
print(momo_amount)
