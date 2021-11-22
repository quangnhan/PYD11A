import requests
import uuid
from tiki import Tiki

class TikiUser(Tiki):
    def __init__(self):
        super().__init__()
        self.endpoint = "users"
    
    def create(self, data):
        return super().create(data)

    