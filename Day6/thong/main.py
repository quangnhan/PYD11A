import uuid
from tiki_user import TikiUser
from tiki_product import TikiProduct

# test exercise 2 users
tiki_user = TikiUser()

data = {"name": "Christine Taylor", "job": "Sailor Moon Girl"}

create_user = tiki_user.create(data)

print(create_user)

# test exercise 2 products
tiki_product = TikiProduct()
data2 = {"item": "vintage bicycle", "quantity": 120}
id = 1
edit_product = tiki_product.edit(id, data2)
data3 = {"item": "Ferrari GTX 2022", "quantity": 100}
create_product = tiki_product.create(data3)

##### From exercise 1
# response = tiki.create_user(data)

# print(response)


# edit_user = tiki.edit_user(data, id)

# delete_user = tiki.delete_user(id)
# get_by_user_id = tiki.get_by_user_id(id)

# print(uuid.uuid1())
