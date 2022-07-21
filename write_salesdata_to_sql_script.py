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

# Use OS to run through excel files
salesdata_path = 'C:\\Users\\kevez\\OneDrive\\Documents\\COMPANIES\\BUYPLUS - PONITEC\\DAILLY SALES'


written_files = open('written_file_names.txt', 'r+')
read_file = written_files.read()

count = 0
new_files = []

for root, dir, files in os.walk(salesdata_path):
    for file in files:

        if file not in read_file:
            try:
                sales_df = pd.read_excel(os.path.join(root, file))

                # Data cleaning
                sales_df['DATE'] = sales_df['DATE'].str.replace("  ", " ")
                sales_df['TIME'] = sales_df['DATE'].str.split(expand=True)[3]
                sales_df['TIME'] = sales_df['TIME'].str.replace('P', 'PM')
                sales_df['TIME'] = sales_df['TIME'].str.replace('A', 'AM')

                sales_df.drop('PROCESSBY', inplace=True, axis=1)
                sales_df.drop('ORDERBY', inplace=True, axis=1)
                sales_df.drop('PARTICULAR', inplace=True, axis=1)
                sales_df.drop('SUPPLIER', inplace=True, axis=1)
                sales_df.drop('CUSTOMERCODE', inplace=True, axis=1)
                sales_df.drop('SALESTYPE', inplace=True, axis=1)
                sales_df.drop('SALESPOINT', inplace=True, axis=1)
                sales_df.drop('VAT', inplace=True, axis=1)

                # Write to table
                sales_df.to_sql('sales1', engine, index=False, if_exists='append')
                written_files.write(f'{file} \n')

                print(f'Successfully written {file} to sales1 table')
                count += 1
                new_files.append(file)

            except PermissionError:
                continue

written_files.close()

if count != 0:
    print('All new files have been written to SQL table')
    print(new_files)
else:
    print('No new files to write to SQL Table')
# %%
