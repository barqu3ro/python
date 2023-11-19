
# d. Otra columna a la que llamaremos d que será la diferencia entre las dos anteriores.
# e. Otra columna a la que llamaremos p. Esta columna será igual a 1 si el registro de la
# columna d es positivo y 0 si es negativo.
# f. Guarda el resultado en un archivo “.csv” separado por “;”.


import pandas as pd
import numpy as np

# crear el data fram en pandas con 201 filas
t = np.arange(0,4.02, 0.02)

# imprimir el data frame
#print (t)

# Aplicar el diccionario 
# a. Una a la que denominaremos t, con los números entre 0 y 4 separados por
# intervalos de 0.02. Es decir: 0, 0.02, 0.04, …, 4
df = pd.DataFrame({'t':t})

# b. Otra con el seno de t a la que llamaremos s.
df['s'] = np.sin(t)

# c. Otra con el seno el valor que tiene el seno de t 10 registros posteriores al que
# llamaremos s10. Sugerencia: El método shift de un data frame de pandas permite
# crear columnas a partir del desplazamiento de la posición de otras.
df['s10'] = df['s'].shift(10)

# d. Otra columna a la que llamaremos d que será la diferencia entre las dos anteriores.
df['d'] = df['s'] - df['s10']

# e. Otra columna a la que llamaremos p. Esta columna será igual a 1 si el registro de la
# columna d es positivo y 0 si es negativo.
df['p'] = np.where(df['d'] > 0, 1, 0)

# f. Guarda el resultado en un archivo “.csv” separado por “;”.

df.to_csv('output.csv', sep=';', index=False)

print(df.head)
