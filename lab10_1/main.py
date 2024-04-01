import pymysql
import time

#функція для виконання окремого SQL-запиту та вимірювання часу його виконання
def execute_query(query):
    try:
        #підключення до бази даних
        conn = pymysql.connect(user='root', password='PHW#84#jeor', host='127.0.0.1', database='video')
        cursor = conn.cursor()

        start_time = time.time()  # Початок вимірювання часу перед виконанням запиту
        cursor.execute(query)
        end_time = time.time()  # Кінець вимірювання часу після виконання запиту
        execution_time = end_time - start_time  # Обчислення часу виконання запиту

        # Виведення результатів запиту
        print("Результати запиту:")
        for row in cursor.fetchall():
            print(row)

        cursor.close()
        conn.close()
        
        return execution_time  # Повертаємо час виконання запиту

    except pymysql.Error as err:
        print(f"Помилка: {err}")
        return None

#функція, яка містить список запитів і виконує кожен запит з цього списку
def perform_queries():
    queries = [
        "SELECT CONCAT(first_name, ' ', last_name) AS full_name, cost * 2 AS bonus FROM actors",
        "SELECT * FROM actors WHERE duration = '01:00:00' OR cost > 3000",
        "SELECT * FROM actors WHERE first_name = 'Дарина' AND NOT date_film = '2022-02-21'",
        "SELECT * FROM actors ORDER BY first_name ASC, cost DESC"
    ]

    for index, query in enumerate(queries, start=1):
        print("\n" + "="*20)  # Відділення запитів лініями
        
        #вимірювання часу перед виконанням запиту та після
        execution_time = execute_query(query)
        if execution_time is not None:
            print(f"Час виконання запиту {index}: {execution_time:.4f} секунд")

if __name__ == "__main__":
    perform_queries()
