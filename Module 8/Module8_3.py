from geopy import distance
import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='123456',
    autocommit=True
)

def get_distance(code1, code2):
    sql1 = "SELECT latitude_deg, longitude_deg FROM airport"
    sql1 += " WHERE ident = '"+code1+"'"
    cursor = connection.cursor()
    cursor.execute(sql1)
    result1 = cursor.fetchone()
    sql2 = "SELECT latitude_deg, longitude_deg FROM airport"
    sql2 += " WHERE ident = '"+code2+"'"
    cursor.execute(sql2)
    result2 = cursor.fetchone()
    co1 = (result1[0], result1[1])
    co2 = (result2[0], result2[1])
    final_result = distance.distance(co1, co2).km
    return final_result

code1 = input("Enter the ICAO code of the first airport:")
code2 = input("Enter the ICAO code of the second airport:")
print(get_distance(code1, code2))

