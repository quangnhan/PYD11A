import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='123456',                             
                             db='shop',) 
        self.cur = self.connection.cursor()

    def get_all_user(self):
        self.cur.execute(f"SELECT * FROM user")
        data = self.cur.fetchall()
        return data

    def get_all_product(self):
        self.cur.execute(f"SELECT * FROM user")
        data = self.cur.fetchall()
        return data