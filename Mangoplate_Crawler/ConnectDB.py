# Database Setting
import psycopg2

hostname = 'localhost'
username = 'hyunsoo_kim'
password = ''
database = 'hyunsoo_kim'

myConnection = psycopg2.connect(
    host=hostname,
    database=database,
    user=username,
    password=password,
)

cur = myConnection.cursor()
cur.execute("SELECT * FROM categories")

print(cur.fetchall())

def doQuery( conn ) :
    cur = conn.cursor()
    cur.execute("SELECT * FROM pricerange")
    for data in cur.fetchall() :
        print(data)