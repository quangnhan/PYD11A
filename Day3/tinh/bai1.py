
name = "tinh@email.com"
class Server:
    def __init__(self, email, full_name, phone_number):
        self.email = email
        self.full_name = full_name
        self.phone_number = phone_number
    
    def get_full_name(self, email):
        if self.email == name:
            print(self.full_name)
            print(self.phone_number)
        else: 
            print("Email khong ton tai")

full = Server("tinh@gmail.com", "Tong Dang Tinh", "0932144")
full.get_full_name()