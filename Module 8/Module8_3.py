from tabulate import tabulate
from geopy import distance
import mysql.connector
from colorama import Fore, Style
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='123456',
    autocommit=True
)

"""def get_distance(code1, code2):
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

#code1 = input("Enter the ICAO code of the first airport:")
#code2 = input("Enter the ICAO code of the second airport:")
#print(get_distance(code1, code2))"""


def store_main_interface():
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, name, passenger_capacity, "
        "flight_range, price, carbon_emission FROM aircraft"
    )
    result = cursor.fetchall()
    headers = ["id", "name", "passenger capacity", "flight range", "price", "carbon emission"]
    table = tabulate(result, headers, tablefmt="grid")
    print(table)


def store_menu(username):
    """
    Display all the planes on sale, include:
        - An ascii picture,
        - Name,
        - Description,
        - Maximum range
        - Carrying capacity
        - Price,
        - Carbon emission coefficient.

    Display sub menu:
    (Store Menu: Enter the plane number to buy, or press Q. Go Back)
    """
    #connection = get_database_connection()
    store_main_interface()
    while True:
        shop_menu_choice = input("For checking aircraft image and purchasing, please enter the aircraft's id.\n"
                                 "For going back to the main menu, please press enter. ")
        cursor = connection.cursor()
        cursor.execute("SELECT balance FROM user "
                       f"WHERE name = '{username}'")
        current_balance = cursor.fetchone()[0]
        print(f"Your current balance is {current_balance}.")
        if not shop_menu_choice:
            break
        try:
            aircraft_id = int(shop_menu_choice)
            if aircraft_id > 0 and aircraft_id < 10:
                cursor = connection.cursor()
                cursor.execute("SELECT image FROM  aircraft WHERE id = %s", (aircraft_id,))
                aircraft_image = cursor.fetchone()
                for item in aircraft_image:
                    print(item)
                aircraft_action = input("1. purchase\n"
                                        "2. Go back to store menu\n")
                try:
                    aircraft_choice = int(aircraft_action)
                    if aircraft_choice == 1:
                        cursor.execute("SELECT aircraft_id, user_id FROM user_aircraft"
                                       " JOIN user ON user.id = user_aircraft.user_id"
                                       f" WHERE name = '{username}'"
                                       f" AND aircraft_id = {aircraft_id}")
                        result = cursor.fetchone()
                        aircraft_repository = None
                        if result is not None:
                            aircraft_repository = result[0]
                            user_id = result[1]
                            print("You already have this plane.")
                        else:

                            cursor.execute("SELECT price FROM aircraft"
                                           f" WHERE id = {aircraft_id}")
                            aircraft_price = float(cursor.fetchone()[0])
                            if aircraft_price:
                                cursor.execute("SELECT balance FROM user"
                                               f" WHERE name = '{username}'")
                                user_balance = float(cursor.fetchone()[0])
                                if user_balance >= aircraft_price:
                                    new_balance = user_balance - aircraft_price
                                    cursor.execute("UPDATE user"
                                                   f" SET balance = {new_balance} "
                                                   f"WHERE name = '{username}'")
                                    cursor.execute(f"SELECT id FROM user WHERE name = '{username}'")
                                    user_id = cursor.fetchone()[0]
                                    cursor.execute("INSERT INTO user_aircraft (user_id, aircraft_id) "
                                                   f"VALUES ({user_id}, {aircraft_id})")
                                    print("Congratulations, you have bought a new plane！")
                                    print(f"Now, your balance is {new_balance}.")
                                else:
                                    print("You do not have enough balance.")
                            else:
                                print("Aircraft not found.")
                    elif aircraft_choice == 2:
                        continue
                    else:
                        print("Invalid input, please enter 1 or 2.")
                except ValueError:
                    print("Invalid input, please enter 1 or 2.")
            else:
                print("Aircraft not found.")
        except ValueError:
            print("Invalid input, please enter 1 to 9.")


username = 'a'


username = 'a'

def ranking_menu(username):
    """
    Display all user ranking, include:
    Sequence    Username    Balance     Amount      Air-miles   Flights
    1           Gary        32332       32332232    2323 km     32
    2           Anqi        3322        30000       323 km      33
    3           Lucas       2323        10000       322 km      22
    ...         ...         ...         ...         ...         ...

    Display sub menu:
    (Ranking Menu: Press Q. Go Back)
    """
    while True:
        #print_header()
        #username = user_info['username']
        #connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT name, total_amount FROM user "
                       "ORDER BY total_amount DESC")
        result = cursor.fetchall()
        ranking_header = cursor.column_names
        ranking_header = ["Ranking"] + [item.replace("_", " ").title()
                                        for item in ranking_header]
        user_row = None
        content = []
        for num, item in enumerate(result, 1):
            row = [num] + list(item)
            content.append(row)
            if item[0] == username:
                user_row = row
                user_row_formatted = [Fore.BLUE + Style.BRIGHT + str(cell) + Style.RESET_ALL for
                                      idx, cell in enumerate(user_row)]
                content[content.index(user_row)] = user_row_formatted
        ranking_table = tabulate(content, ranking_header, tablefmt="grid")
        #print_title('ranking')
        print(ranking_table)
        choice = input("Press enter to go back to the main menu.")
        if not choice:
            break


ranking_menu('a')
print(Fore.BLUE + Style.BRIGHT + "This is a bold string" + Style.RESET_ALL)