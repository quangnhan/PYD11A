from products import ProductController

p = ProductController()

data = {
    "id": 5,
    "name": "Bicycle",
    "price": 500,
}
p.insert(data)

rows = p.get_all()
for r in rows:
    print(r)