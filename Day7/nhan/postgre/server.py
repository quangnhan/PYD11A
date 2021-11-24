import psycopg2


class Server:
    def __init__(self):
        self.conn = psycopg2.connect(database="shop",
                                     user="postgres",
                                     password="admin",
                                     host="127.0.0.1",
                                     port="5432")
        self.cur = self.conn.cursor()

    def get_all(self):
        self.cur.execute(f"SELECT * FROM public.{self.table}")
        data = self.cur.fetchall()
        return data

    def insert(self, data):
        self.cur.execute(
            f"""INSERT INTO public.products (id, name, price) 
            VALUES ({data['id']}, '{data['name']}', {data['price']});""")
        self.conn.commit()
