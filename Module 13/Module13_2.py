import json

from flask import Flask, jsonify
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='123456',
    autocommit=True
)

app = Flask(__name__)


def get_airport_information(code):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident = '"+code+"'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


@app.route('/airport/<code>', methods=['GET'])
def print_information(code):
    information = get_airport_information(code)
    name, municipality = information[0]
    answer = {
        "ICAO": code,
        "Name": name,
        "Location": municipality
    }
    return jsonify(answer)


if __name__ == '__main__':
    app.run(debug=True)
