CUSTOMERS = {
    'nhan@gmail.com': {
        'phone': '123123',
        'full_name': 'Vo Quang Nhan',
    },
    'thong@gmail.com': {
        'phone': '123123',
        'full_name': 'Tran Quoc Thong',
    },
    'tinh@gmail.com': {
        'phone': '123123',
        'full_name': 'Tong Dang Tinh',
    }
}

class Server:
    def get_full_name(self, email):
        full_name = "This email doesn't exist"

        if CUSTOMERS.get(email):
            full_name = CUSTOMERS[email]['full_name']
        
        return full_name

if __name__ == "__main__":
    server = Server()
    email = 'nhan@gmail.com'
    full_name = server.get_full_name(email)
    print(full_name)