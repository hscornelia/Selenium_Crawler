# Database Setting
import psycopg2
from datetime import datetime

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

    # 여기에 restaurant table 추가 쿼리
    # 나중에 조금더 추상화
    def addRestaurant(self, restaurantInfo):
        cur_time = datetime.today().strftime('%Y-%m-%d')

        ConnectDB.cursor.execute(
            "INSERT INTO restaurants \
             ( \
                name, \
                address, \
                business_hour, \
                parking_space,\
                created_at, \
                updated_at, \
                location, \
                pricerange,\
                category, \
                point \
            ) \
             VALUES \
            ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (name) DO NOTHING; COMMIT; ", \
            (
                restaurantInfo.get('name'),
                restaurantInfo.get('address'), 
                restaurantInfo.get('business_hour'), 
                restaurantInfo.get('parking_space'), 
                cur_time, 
                cur_time, 
                restaurantInfo.get('location'), 
                restaurantInfo.get('pricerange'), 
                restaurantInfo.get('category'), 
                restaurantInfo.get('point'), 
            )
        )
        print(restaurantInfo)