import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(database="shop",
                                     user="postgres",
                                     password="admin",
                                     host="127.0.0.1",
                                     port="5432")
        self.cur = self.conn.cursor()

    def get_all_user(self):
        self.cur.execute(f"SELECT * FROM public.user")
        data = self.cur.fetchall()
        return data

    def insert_user(self, data):
        self.cur.execute(
            f"""INSERT INTO public.user (id, ten, tuoi) 
            VALUES ({data['id']}, '{data['name']}', {data['age']});""")
        self.conn.commit()
