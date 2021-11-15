from momo_server import MoMoServer
from vnpay_server import VNPayServer
from zalopay_server import ZaloPayServer

class PaymentApp:
    amount = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def pay(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            print(f"Confirm payment of {amount}")
        else:
            print("Your retain is not enough")

    def say_hi(self):
        print(f"Hello {self.username}")

class Momo(PaymentApp):
    discount = 0.15

    def __init__(self, username, password):
        super().__init__(username, password)
        server = MoMoServer()
        self.amount = float(server.get_amount(username, password))

    def say_hi(self):
        print(f"Momo hello {self.username}")

class VNPay(PaymentApp):
    def __init__(self, username, password):
        super().__init__(username, password)
        server = VNPayServer()
        self.amount = float(server.get_amount(username, password))


class ZaloPay(PaymentApp):
    def __init__(self, username, password):
        super().__init__(username, password)
        server = ZaloPayServer()
        self.amount = float(server.get_amount(username, password))


user = Momo("username 2", "password 2")
# user = Momo("username 2", "password 2")
# user = VNPay("username 2", "password 2")
# print(user.amount)
# user.pay(100)

user.say_hi()