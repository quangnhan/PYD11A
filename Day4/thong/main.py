class PaymentApp:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.amount = 0

    def pay(self, amount):
        self.amount = amount
        print(f"Confirm payment of {amount}")


class Momo(PaymentApp):
    pass


class VNPay(PaymentApp):
    pass


class Zalo_Pay(PaymentApp):
    pass


momo = Momo("thongqt", "password123")
momo.pay(123.00)
