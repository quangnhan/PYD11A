from momo_server import MoMoServer
from zalopay_server import ZaloPayServer
from vnpay_server import VNPayServer


class PaymentApp:
    amount = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def pay(self, amount):
        if self.amount >= amount:
            self.amount -= amount

            print(f"Confirm payment of {amount}.00 USD")
        else:
            print("Not enough money bro")


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


class ZaloPay(PaymentApp):
    def __init__(self, username, password):
        super().__init__(username, password)
        server = ZaloPayServer()
        self.amount = float(server.get_amount(username, password))


user_momo = Momo("username 3", "password 3")
print(f"Your Momo walle has {user_momo.amount} USD")

user_vnpay = VNPay("username 3", "password 3")
print(f"Your VNPay wallet has {user_vnpay.amount} USD")

user_zalopay = ZaloPay("username 3", "password 3")
print(f"Your Zalo Pay has {user_zalopay.amount} USD")

user_momo.pay(102)