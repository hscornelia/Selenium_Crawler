# Database Setting
import psycopg2

class ConnectDB:

    hostname = 'localhost'
    username = 'sangchulkim'
    password = ''
    database = 'restaurant_api_development'
    myConnection = psycopg2.connect(
        host = hostname,
        database = database,
        user = username,
        password = password
    )
    cursor = myConnection.cursor()
    
    def __init__(self):
        pass

    def getRestaurant(self):
        ConnectDB.cursor.execute("SELECT * FROM categories")
        print(ConnectDB.cursor.fetchall())

    def addRestaurant(self, restaurantInfo):
        print(restaurantInfo)
        pass