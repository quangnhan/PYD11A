from server import Server

class Momo:
    def __init__(self, email):
        server = Server()
        
        self.email = email
        self.full_name = server.get_full_name(email)

        print(f"Hello {self.full_name}")

if __name__ == "__main__":
    momo = Momo("nhan@gmail.com")
    


