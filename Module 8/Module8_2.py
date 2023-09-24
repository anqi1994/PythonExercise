import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='123456',
    autocommit=True
)

def get_airport_type(area_code):
    sql = "SELECT name, type FROM airport"
    sql +=" WHERE iso_country = '"+area_code+"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        return result


airportlist = (get_airport_type('FI'))
sorted_list = sorted(airportlist, key=lambda x: x[1])
for airport in sorted_list:
    print(airport)