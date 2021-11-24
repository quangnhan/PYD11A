from server import Server


class ProductController(Server):
    def __init__(self):
        super().__init__()
        self.table = "products"
