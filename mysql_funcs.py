# %%
import mysql.connector
import pandas as pd


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




# %%
