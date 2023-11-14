import os
import pandas as pd

# Get the current working directory
cwd = os.getcwd()

# Define the relative path to the csv file
csv_path = os.path.join(cwd, 'data', 'big_bang_theory_dataset.csv')

# Load the csv file into a pandas dataframe
df = pd.read_csv(csv_path)




print(os.getcwd())

df.head()



# # Define the MySQL database details
# username = 'root'
# password = 'TESTDBPWD01'
# host = 'localhost'
# port = '3306'
# database = 'my-mysql'

# # Create the connection string
# connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

# # Create the database connection
# engine = create_engine(connection_string)

# # Create the table
# df.to_sql('big_bang_theory_dataset', engine, index=False, if_exists='replace')

# # Read the table
# df = pd.read_sql('big_bang_theory_dataset', engine)

# # Show the table
# print(df)


# ## Estoy recibiendo access denied --- mañana sigo avanzando 