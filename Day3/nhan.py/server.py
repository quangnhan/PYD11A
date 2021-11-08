class Server:
    def __init__(self, name):
        self.name = name

    def say_hi(self, email):
        print(f"Hello {email} -- {self.name}")

if __name__ == "__main__":
    server = Server("Server 1 server")
    server.say_hi("quangnhan@gmail.com")