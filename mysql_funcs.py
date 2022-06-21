# %%
import mysql.connector


def create_server_connection(host_name, user_name, user_password):
    connecton = None

    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )

        print('MySQL Database connection successful')
    except mysql.connector.Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('Database created successfully')
    except mysql.connector.Error as err:
        print(f"Error: '{err}")


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None

    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")

    except mysql.connector.Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor(buffered=True)

    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")

    except mysql.connector.Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print('Query Successful')
        return result
    except mysql.connector.Error as err:
        print(f"Error: '{err}'")
# %%
