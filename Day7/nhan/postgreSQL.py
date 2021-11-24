import psycopg2

conn = psycopg2.connect(database="shop", 
                        user="postgres",
                        password="admin",
                        host="127.0.0.1", 
                        port="5432")

cur = conn.cursor()

cur.execute("INSERT INTO public.products (id, name, price) VALUES (3, 'T-Shirt', 200);")
cur.execute("SELECT * FROM public.products")
rows = cur.fetchall()
for row in rows:
   print(row)

conn.commit()
conn.close()