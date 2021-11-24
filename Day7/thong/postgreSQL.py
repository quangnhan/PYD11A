import psycopg2

conn = psycopg2.connect(
    database="shop-django",
    user="postgres",
    password="Abcd@1234",
    host="127.0.0.1",
    port="5432",
)

cur = conn.cursor()

cur.execute("SELECT * FROM public.users")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()