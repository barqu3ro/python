# Conecta a esa base de datos con pyodbc o SQL Alchemy. Crea una tabla en la base
# de datos desde un data frame de pandas creado a partir de los datos del fichero
# big_bang_theory_dataset.csv que hay en el aula virtual.



#create a data frame using the csv file in this folder
import pandas as pd
#import pyodbc
import sqlalchemy
import urllib 

# Create a dataframe from the csv file
df = pd.read_csv('big_bang_theory_dataset.csv')

df.head()