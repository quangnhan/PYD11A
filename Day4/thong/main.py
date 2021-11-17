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

            print(f"Confirm payment of {amount} USD")
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
            self.amount -= amount * (1 - discount)

            print(
                f"Confirm payment of {amount - amount*discount}, remaining balance is {self.amount}"
            )
        else:
            print("Not enough money bro")


class VNPay(PaymentApp):
    __log = []

    def __init__(self, username, password):
        super().__init__(username, password)
        server = VNPayServer()
        self.amount = float(server.get_amount(username, password))

    def pay(self, amount):
        # PaymentApp.pay(amount) # doesn't work #why?
        if self.amount >= amount:
            self.amount -= amount

            print(f"Confirm payment of {amount} USD")
        else:
            print("Not enough money bro")

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
        # PaymentApp.pay(amount) # doesn't work

        if self.amount >= amount:
            self.order = self.order + 1
            if self.order % 11 == 0:
                self.amount -= amount * (1 - discount)

                print(
                    f"Payment of {amount * (1-discount)} USD, remaining balance is {self.amount}, order no. {self.order}."
                )
            else:
                self.amount -= amount

                print(
                    f"Confirm payment of {amount} USD, remaining balance is {self.amount}, order no. {self.order}."
                )
        else:
            print("Not enough money bro")


# exercise 1
# user_momo = Momo("username 3", "password 3")
# print(f"Your Momo walleT has {user_momo.amount} USD")

# user_vnpay = VNPay("username 3", "password 3")
# print(f"Your VNPay wallet has {user_vnpay.amount} USD")

user_zalopay = ZaloPay("username 2", "password 2")
print(f"Your Zalo Pay has {user_zalopay.amount} USD")


# exercise 3

# user_momo.pay(100)
# user_vnpay.pay(200)
# user_vnpay.get_log()


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
# order number 21
user_zalopay.pay(10)
# order number 22
user_zalopay.pay(10)