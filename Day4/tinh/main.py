from momo_server import MoMoServer
from zalopay_server import ZaloPayServer
from vnpay_server import VNPayServer

from datetime import datetime


class PaymentApp:
    amount = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.log = list()

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

    def pay(self, amount):
        discount = 0.2
        if self.amount >= amount:
            self.amount -= amount * discount

            print(
                f"Confirm payment of {amount - amount*0.2}.00 USD, remaining balance is {self.amount}"
            )
        else:
            print("Not enough money bro")


class VNPay(PaymentApp):
    log = []

    def __init__(self, username, password):
        super().__init__(username, password)
        server = VNPayServer()
        self.amount = float(server.get_amount(username, password))

    def pay(self, amount):

        if self.amount >= amount:
            self.amount -= amount

            print(
                f"Confirm payment of {amount}.00 USD, remaining balance is {self.amount}"
            )
        else:
            print("Not enough money bro")

        self.log_payment(
            f"{self.username} made payment of {self.amount} at {str(datetime.now())}"
        )

    def log_payment(self, message):
        self.log.append(message)

    def get_log(self):
        for log in self.__log:
            print(log)


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

user_momo.pay(100)
user_vnpay.pay(250)
