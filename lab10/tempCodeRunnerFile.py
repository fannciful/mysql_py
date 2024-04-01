import mysql.connector
import time

def execute_query(query):
    try:
        conn = mysql.connector.connect(user='root', password='PHW#84#jeor', host='127.0.0.1', database='video')
        cursor = conn.cursor()

        cursor.execute(query)
        
        print("Результати запиту:")
        for row in cursor.fetchall():
            print(row)

        cursor.close()
        conn.close()
        
    except mysql.connector.Error as err:
        print(f"Помилка: {err}")

def perform_queries():
    queries = [
        "SELECT CONCAT(first_name, ' ', last_name) AS full_name, cost * 2 AS bonus FROM actors",
        "SELECT * FROM actors WHERE duration = '01:00:00' OR cost > 3000",
        "SELECT * FROM actors WHERE first_name = 'Дарина' AND NOT date_film = '2022-02-21'",
        "SELECT * FROM actors ORDER BY first_name ASC, cost DESC"
    ]

    for index, query in enumerate(queries, start=1):
        print("\n" + "="*20)  # Відділення запитів лініями
        
        start_time = time.time()  # Початок вимірювання часу виконання запиту
        execute_query(query)
        execution_time = time.time() - start_time  # Обчислення часу виконання запиту

        print(f"Час виконання запиту {index}: {execution_time:.4f} секунд")

if __name__ == "__main__":
    perform_queries()
