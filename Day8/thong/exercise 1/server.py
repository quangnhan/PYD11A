import requests
import psycopg2


class UserAPI:
    def __init__(self):
        self.url = "https://619b87292782760017445671.mockapi.io/"
        self.endpoint = "students"

    def get_all(self):
        response = requests.get(f"{self.url}/{self.endpoint}")
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
        self.table = "students"

    def get_all(self):
        self.cur.execute(f"SELECT * FROM public.{self.table}")
        data = self.cur.fetchall()
        return data

    def insert(self, data):
        self.cur.execute(
            f"""INSERT INTO public.students (id,name, age)
            VALUES ({data['id']}, '{data['name']}', {data['age']});"""
        )
        self.conn.commit()
