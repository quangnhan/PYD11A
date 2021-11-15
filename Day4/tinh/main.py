class Human:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class MoMo(Human):
    def pay(self, mount_momo):
        self.mount_momo = mount_momo 


class VNPay(Human):
    def pay(self, mount_vnpay):
        self.mount_vnpay = mount_vnpay

class ZaloPay(Human):
    def pay(self, mount_zalopay):
        self.mount_zalopay = mount_zalopay


zalo = ZaloPay("Tinh","01929")
print(zalo)

print(zalo.pay(100))