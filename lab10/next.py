import mysql.connector
import random
import string
import time

def add_random_records(table_name, num_records):
    server = '127.0.0.1'
    user = 'root'
    password = 'PHW#84#jeor'
    database = 'video'

    try:
        conn = mysql.connector.connect(user=user, password=password, host=server, database=database)
        cursor = conn.cursor()

        for _ in range(num_records):
            random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            query = f"INSERT INTO {table_name}(surname) VALUES ('{random_data}')"
            cursor.execute(query)

        conn.commit()
        print(f"{num_records} записів було успішно додано до таблиці {table_name}")

        query_show = f"SELECT * FROM {table_name}"
        cursor.execute(query_show)
        print(f"Вміст таблиці {table_name}:")
        for row in cursor:
            print(row)

    except mysql.connector.Error as err:
        print(f"Помилка: {err}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def measure_query_time(query_function, *args):
    start_time = time.time()
    result = query_function(*args)
    execution_time = time.time() - start_time
    return result, execution_time

def query_with_alias_and_functions(cursor):
    query = "SELECT CONCAT (first_name, ' ', last_name) AS full_name, cost * 2 AS bonus FROM actors"
    cursor.execute(query)

    print("\nРезультати запиту з псевдонімами та функціями:")
    for row in cursor:
        print(row)

def query_with_filters(cursor):
    query = "SELECT * FROM actors WHERE duration = '01:00:00' OR cost > 3000"
    cursor.execute(query)

    print("\nРезультати запиту з фільтрацією:")
    for row in cursor:
        print(row)

def query_with_logical_operators(cursor):
    query = "SELECT * FROM actors WHERE first_name = 'Дарина' AND NOT date_film = '2022-02-21'"
    cursor.execute(query)

    print("\nРезультати запиту з логічними операторами:")
    for row in cursor:
        print(row)

def query_with_sorting(cursor):
    query = "SELECT * FROM actors ORDER BY first_name ASC, cost DESC"
    cursor.execute(query)

    print("\nРезультати запиту з сортуванням:")
    for row in cursor:
        print(row)

if name == "main":
    table_name = 'information'
    add_random_records(table_name, 1)

    user = 'root'
    password = 'PHW#84#jeor'
    server = '127.0.0.1'
    database = 'video'

    try:
        conn = mysql.connector.connect(user=user, password=password, host=server, database=database)
        cursor = conn.cursor()

        functions = [
            query_with_alias_and_functions,
            query_with_filters,
            query_with_logical_operators,
            query_with_sorting
        ]

        for query_function in functions:
            result, execution_time = measure_query_time(query_function, cursor)
            print(f"\nЧас виконання запиту: {execution_time} секунд")
            
    except mysql.connector.Error as err:
        print(f"Помилка: {err}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()