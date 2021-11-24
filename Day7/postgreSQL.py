import psycopg2

conn = psycopg2.connect(database="shop", 
                        user="postgres",
                        password="admin",
                        host="127.0.0.1", 
                        port="5432")

cur = conn.cursor()

cur.execute("SELECT * FROM public.products")
rows = cur.fetchall()
for row in rows:
   print(row)

conn.close()