from users import UsersManager

p = UsersManager()
data = {
    "id": 3,
    "name": "Clark Kent",
    "phone": 50231,
}
p.insert(data)

rows = p.get_all()
for r in rows:
    print(r)