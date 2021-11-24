from tiki import Tiki

class TikiProduct(Tiki):
    def __init__(self):
        super().__init__()
        self.endpoint = "products"

    