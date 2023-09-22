import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='123456',
    autocommit=True
)

def getAirportInformation(code):
    sql = "SELECT name, municipality FROM airport"
    sql +=" WHERE ident = '"+code+"'"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        print(result)
    return

code = input("ICAO:")
getAirportInformation(code)
