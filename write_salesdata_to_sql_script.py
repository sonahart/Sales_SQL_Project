# %%
import os
import mysql_funcs as myf
import pandas as pd
import numpy as np
import sqlalchemy as sqa

# Establish server connection for mysql_funcs
import getpass as gp
passkey = gp.getpass()
connection = myf.create_server_connection('localhost', 'root', passkey)

# Establish connection for sqlalchemy
url = f'mysql://root:{passkey}@localhost/buyplus_sales'
engine = sqa.create_engine(url, echo=True)

# Create Database
create_database_query = "CREATE DATABASE if not exists buyplus_sales"
myf.create_database(connection, create_database_query)

# Connect to Database
connection = myf.create_db_connection(
    "localhost", 'root', passkey, 'buyplus_sales')


# Import OS to run through excel files
salesdata_path = 'C:\\Users\\kevez\\OneDrive\\Documents\\COMPANIES\\BUYPLUS - PONITEC\\DAILLY SALES'

written_files = open('written_file_names.txt', 'a+')
read_file = written_files.read()

for root, dir, files in os.walk(salesdata_path):
    for file in files:
        if file in read_file:
            pass
        else:
            sales_df = pd.read_excel(os.path.join(root, file))

            # Data cleaning
            sales_df['DATE'] = sales_df['DATE'].str.replace("  ", " ")
            sales_df['TIME'] = sales_df['DATE'].str.split(expand=True)[3]
            sales_df['TIME'] = sales_df['TIME'].str.replace('P', 'PM')
            sales_df['TIME'] = sales_df['TIME'].str.replace('A', 'AM')

            # Write to table
            sales_df.to_sql('sales1', engine, index=False, if_exists='append')
            written_files.write(f'{file} \n')

            print(f'Successfully written {file} to sales1 table')

written_files.close()

# %%
