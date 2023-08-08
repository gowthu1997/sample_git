import mysql.connector

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS my_sample_db")
    cursor.close()

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("USE my_sample_db")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age INT
        )
    """)
    cursor.close()

def insert_record(connection, cursor):
    query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
    values = ("John Doe", "john@example.com", 30)
    cursor.execute(query, values)
    connection.commit()

def retrieve_records(connection, cursor):
    query = "SELECT * FROM users"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)

if __name__ == "__main__":
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Gowthu@1997"
        )
        
        create_database(connection)
        create_table(connection)

        connection.database = "my_sample_db"  # Switch to the created database
        cursor = connection.cursor()

        insert_record(connection, cursor)
        retrieve_records(connection, cursor)

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")
