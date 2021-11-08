orders = [
    {"customer": "Nhan", "product": 1, "quantity": 3},
    {"customer": "Nathan", "product": 9, "quantity": 20},
]

product_list = [
    {
        "name": "Hat",
        "image": "http://placeimg.com/640/480/nightlife",
        "price": "37.00",
        "id": "1",
        "categoryid": "1",
    },
    {
        "name": "Chips",
        "image": "http://placeimg.com/640/480/people",
        "price": "333.00",
        "id": "5",
        "categoryid": "1",
    },
    {
        "name": "Table",
        "image": "http://placeimg.com/640/480/cats",
        "price": "13.00",
        "id": "9",
        "categoryid": "1",
    },
    {
        "name": "Tuna",
        "image": "http://placeimg.com/640/480/abstract",
        "price": "987.00",
        "id": "13",
        "categoryid": "1",
    },
    {
        "name": "Bacon",
        "image": "http://placeimg.com/640/480/fashion",
        "price": "228.00",
        "id": "17",
        "categoryid": "1",
    },
    {
        "name": "Ball",
        "image": "http://placeimg.com/640/480/nightlife",
        "price": "793.00",
        "id": "21",
        "categoryid": "1",
    },
    {
        "name": "Keyboard",
        "image": "http://placeimg.com/640/480/business",
        "price": "624.00",
        "id": "25",
        "categoryid": "1",
    },
    {
        "name": "Hat",
        "image": "http://placeimg.com/640/480/nightlife",
        "price": "756.00",
        "id": "29",
        "categoryid": "1",
    },
    {
        "name": "Shoes",
        "image": "http://placeimg.com/640/480/transport",
        "price": "284.00",
        "id": "33",
        "categoryid": "1",
    },
    {
        "name": "Ball",
        "image": "http://placeimg.com/640/480/city",
        "price": "838.00",
        "id": "37",
        "categoryid": "1",
    },
    {
        "name": "Fish",
        "image": "http://placeimg.com/640/480/people",
        "price": "996.00",
        "id": "41",
        "categoryid": "1",
    },
    {
        "name": "Table",
        "image": "http://placeimg.com/640/480/transport",
        "price": "926.00",
        "id": "45",
        "categoryid": "1",
    },
    {
        "name": "Chips",
        "image": "http://placeimg.com/640/480/cats",
        "price": "416.00",
        "id": "49",
        "categoryid": "1",
    },
    {
        "name": "Chair",
        "image": "http://placeimg.com/640/480/cats",
        "price": "959.00",
        "id": "53",
        "categoryid": "1",
    },
    {
        "name": "Fish",
        "image": "http://placeimg.com/640/480/abstract",
        "price": "756.00",
        "id": "57",
        "categoryid": "1",
    },
    {
        "name": "Chips",
        "image": "http://placeimg.com/640/480/business",
        "price": "655.00",
        "id": "61",
        "categoryid": "1",
    },
    {
        "name": "Sausages",
        "image": "http://placeimg.com/640/480/sports",
        "price": "158.00",
        "id": "65",
        "categoryid": "1",
    },
    {
        "name": "Salad",
        "image": "http://placeimg.com/640/480/city",
        "price": "464.00",
        "id": "69",
        "categoryid": "1",
    },
    {
        "name": "Car",
        "image": "http://placeimg.com/640/480/technics",
        "price": "276.00",
        "id": "73",
        "categoryid": "1",
    },
    {
        "name": "Chicken",
        "image": "http://placeimg.com/640/480/animals",
        "price": "165.00",
        "id": "77",
        "categoryid": "1",
    },
    {
        "name": "Tuna",
        "image": "http://placeimg.com/640/480/fashion",
        "price": "283.00",
        "id": "81",
        "categoryid": "1",
    },
    {
        "name": "Bike",
        "image": "http://placeimg.com/640/480/animals",
        "price": "147.00",
        "id": "85",
        "categoryid": "1",
    },
    {
        "name": "Car",
        "image": "http://placeimg.com/640/480/cats",
        "price": "185.00",
        "id": "89",
        "categoryid": "1",
    },
    {
        "name": "Shirt",
        "image": "http://placeimg.com/640/480/technics",
        "price": "109.00",
        "id": "93",
        "categoryid": "1",
    },
    {
        "name": "Pizza",
        "image": "http://placeimg.com/640/480/food",
        "price": "15.00",
        "id": "97",
        "categoryid": "1",
    },
]


order_total = []

for product in product_list:
    for order in orders:
        if order["product"] == int(product["id"]):
            total = order["quantity"] * float(product["price"])
            order_total.append(total)

print("order_total: ", order_total)