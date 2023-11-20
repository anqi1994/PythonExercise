import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='123456',
         autocommit=True
         )
def get_data(sql):
    #sql = "SELECT * FROM game"
    cursor = connection.cursor()
    cursor.execute(sql)
    names = cursor.column_names
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        return [dict(zip(names, row)) for row in result]

sql = "SELECT * FROM game"
res = get_data(sql)
print(res)