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
    
    def discount(self, don_hang, gia_hang):
        pay_total = 0
        self.don_hang = don_hang
        self.gia_hang = gia_hang
       
        if don_hang > 0:
            pay_total = (don_hang * gia_hang *20)/100
            print(pay_total)
        else:
            print("Ban khong mua hang nen ko duoc giam gia")
            

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
print(user.discount(0,0))

# user = VNPay("username 2", "password 2")
# print(user.amount)

# user = Zalo_Pay("username 2", "password 2")
# print(f"so du {user.amount}")