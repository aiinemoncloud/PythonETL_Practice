import sqlite3
import pandas as pd
conn = sqlite3.connect('STAFF.db') #created a STAFF database

#creating and loading table
table_name = "INSTRUCTOR"
attribute_list = ['ID','FNAME',"LNAME","CITY","CCODE"]

#Reading the file
file_path = "/home/project/INSTRUCTOR.csv"
df = pd.read_csv(file_path, names = attribute_list)

df.to_sql(table_name, conn, if_exists = 'replace', index = False)
print('Table is ready')

#Running Basic Queries
query_statement = f'SELECT * FROM {table_name}'
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#viewing only FNAME column of data
query_statement2 = f'SELECT * FROM {table_name}'
query_output2 = pd.read_sql(query_statement2, conn)
print(query_statement2)
print(query_output2)

# viewing total number of entries in table
query_statement3 = f"SELECT COUNT(*) FROM {table_name}"
query_output3 = pd.read_sql(query_statement3, conn)
print(query_statement3)
print(query_output3)

#appending data to the table
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

#finally we close the connection
conn.close()