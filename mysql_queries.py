import mysql_funcs as myf


# Establish server connection
passkey = input('Enter server password: ')
connection = myf.create_server_connection('localhost', 'root', passkey)

# Create Database
create_database_query = "CREATE DATABASE buyplus_sales if not exists"
myf.create_database(connection, create_database_query)
