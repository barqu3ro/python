# Conecta a esa base de datos con pyodbc o SQL Alchemy. Crea una tabla en la base
# de datos desde un data frame de pandas creado a partir de los datos del fichero
# big_bang_theory_dataset.csv que hay en el aula virtual.



#create a data frame using the csv file in this folder
import pandas as pd
import os
#import pyodbc
import sqlalchemy
import urllib 
from sqlalchemy import create_engine

# leer el fichero csv
df = pd.read_csv('/Users/jorgebarquero/GitRepos/python/Estudio/Intro-python/Modulo2/data/big_bang_theory_dataset.csv')

print(os.getcwd())

#df.head()



# Define the MySQL database details
username = 'root'
password = 'TESTDBPWD01'
host = 'localhost'
port = '3306'
database = 'my-mysql'

# Create the connection string
connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

# Create the database connection
engine = create_engine(connection_string)

# Create the table
df.to_sql('big_bang_theory_dataset', engine, index=False, if_exists='replace')

# Read the table
df = pd.read_sql('big_bang_theory_dataset', engine)

# Show the table
print(df)


## Estoy recibiendo access denied --- mañana sigo avanzando 