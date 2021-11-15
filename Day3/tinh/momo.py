from server import Server

class MOMO:
    def __init__(self, email):
        server = Server()
        self.email = email
        self.full_name = server.get_full_name(email)
    
        print(f"Hello {self.full_name}")

if __name__ == "__main__":
    momo = MOMO("tinh@gmail.com")
    momo2 = MOMO("nhan@gmail.com")
    
    