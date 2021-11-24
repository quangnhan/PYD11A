from products import ProductController

p = ProductController()
data = {
    "id": 5,
    "name": "Nhan",
    "price": 50,
}
p.insert(data)

rows = p.get_all()
for r in rows:
    print(r)