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
            print(f"So du {amount}")
        else:
            print("So du cua ban khong du")

class Momo(PaymentApp):
    def __init__(self, username, password):
        super().__init__(username, password)
        server = MoMoServer()
        self.amount = float(server.get_amount(username, password))

class VNPay(PaymentApp):
    def __init__(self, username, password):
        super().__init__(username, password)
        server = VNPayServer()
        self.amount = float(server.get_amount(username, password))


class Zalo_Pay(PaymentApp):
    def __init__(self, username, password):
        super().__init__(username, password)
        server = ZaloPayServer()
        self.amount = float(server.get_amount(username, password))

user = Momo("username 2", "password 2")
print(user.amount)
user = VNPay("username 2", "password 2")
print(user.amount)

user = Zalo_Pay("username 2", "password 2")
print(f"so du {user.amount}")