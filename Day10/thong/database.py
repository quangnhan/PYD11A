import psycopg2


class Database:
    def __init__(self):

        self.conn = psycopg2.connect(
            database="day9",
            user="postgres",
            password="Abcd@1234",
            host="127.0.0.1",
            port="5432",
        )
        self.cur = self.conn.cursor()

    def get_all_user(self):
        self.cur.execute(f"SELECT * FROM users")
        data = self.cur.fetchall()
        return data

    def get_all_product(self):
        self.cur.execute(
            """
        SELECT product.id, category.id, category.name, product.name FROM product
        INNER JOIN category ON category.id = product.category_id"""
        )
        data = self.cur.fetchall()
        return data
