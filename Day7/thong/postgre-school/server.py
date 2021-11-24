import psycopg2


class Server:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="school",
            user="postgres",
            password="Abcd@1234",
            host="127.0.0.1",
            port="5432",
        )
        self.cur = self.conn.cursor()

    def get_all(self):
        self.cur.execute(f"SELECT * FROM public.{self.table}")
        data = self.cur.fetchall()
        return data

    def insert(self, data):
        self.cur.execute(
            f"""INSERT INTO public.users (id, name, phone) 
            VALUES ({data['id']}, '{data['name']}', {data['phone']});"""
        )
        self.conn.commit()
