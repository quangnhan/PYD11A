import requests
import psycopg2


class UserAPI:
    def __init__(self):
        self.url = "https://619b87292782760017445671.mockapi.io/"

    def get_all(self, endpoint):
        response = requests.get(f"{self.url}/{endpoint}")
        data = response.json()
        return data


class UserDatabase:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="day8",
            user="postgres",
            password="Abcd@1234",
            host="127.0.0.1",
            port="5432",
        )
        self.cur = self.conn.cursor()
        self.table = "mixed_users"

    def get_all(self):
        self.cur.execute(f"SELECT * FROM public.{self.table}")
        data = self.cur.fetchall()
        return data

    def insert(self, data):
        self.cur.execute(
            f"""INSERT INTO public.mixed_users (id,ten, tuoi)
            VALUES ({data['id']}, '{data['ten']}', {data['tuoi']});"""
        )
        self.conn.commit()
