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

            print(f"Confirm payment of {amount}")
        else:
            print("Not enough money")


class Momo(PaymentApp):
    def __init__(self, username, password):
        super().__init__(username, password)
        server = MoMoServer()
        self.amount = float(server.get_amount(username, password))

    def pay(self, amount):
        super().pay(amount*0.8)

class VNPay(PaymentApp):
    __log = []

    def __init__(self, username, password):
        super().__init__(username, password)
        server = VNPayServer()
        self.amount = float(server.get_amount(username, password))

    def pay(self, amount):
        super.pay(amount)
        self.__log_payment(
            f"{self.username} made payment of {amount}, and remaining balance of {self.amount} at {str(datetime.now())}"
        )

    def __log_payment(self, message):
        self.__log.append(message)

    def get_log(self):
        for log in self.__log:
            print(log)


class ZaloPay(PaymentApp):
    def __init__(self, username, password):
        super().__init__(username, password)
        server = ZaloPayServer()
        self.amount = float(server.get_amount(username, password))
        self.order = 0

    def pay(self, amount):
        discount = 0.7

        if (self.order == 11):
            super().pay(amount)
            self.order = 0
            return
        super().pay(amount*(1-discount))
        self.order = self.order + 1
        



# exercise 1 + exercise 2
# user_momo = Momo("username 3", "password 3")
# print(f"Your Momo walleT has {user_momo.amount} USD")

# user_vnpay = VNPay("username 3", "password 3")
# print(f"Your VNPay wallet has {user_vnpay.amount} USD")

user_zalopay = ZaloPay("username 2", "password 2")
print(f"Your Zalo Pay has {user_zalopay.amount}")


# exercise 3 - momo discount

# user_momo.pay(100)

# exercise 3 - vnpay log
# user_vnpay.pay(200)
# user_vnpay.get_log()


# exercise 3 - zalo pay discount on 11th order
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
# order number 11
user_zalopay.pay(10)
user_zalopay.pay(10)

user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
user_zalopay.pay(10)
# order number 22
user_zalopay.pay(10)