 # God mode:
# (3 puntos) El número de Sheldon: En la serie “Big Bang Theory” se conjeturó que el número
# 23 posee unas características únicas que no posee ningún otro número (link a la conjetura
# original). En 2019 Pomerance y Spicer demostraron que solo el 73 cumple las condiciones de
# la Conjetura de Sheldon (link a la desmostración). El ejercicio consistirá en comprobar que
# en los números entre el 1 y el 1 000 000 solo el 73 cumple la conjetura de Sheldon. Un
# número de Sheldon debe cumplir 3 propiedades:
# a. Es primo.
# b. El producto de sus dígitos [llamemos a esta operación m()] es igual a su posición en
# la lista de todos los primos (empezando por el número 2). Por ejemplo: En 73, m(73)
# = 7*3 = 21 y en la lista de primos el 73 está en la posición 21ª (se puede comprobar
# con el ejercicio 6).
# c. El número espejo de otro será el conseguido al invertir el orden de las [llamemos a
# esta operación r()]. El primo en la posición de su número espejo es igual al número
# espejo de su posición. Por ejemplo: r(73) = 37, la posición del 37 es la doceava, el
# espejo de 12 es 21 y el número primo en la posición 21ª es el 73.


# Lista de números primos
primos = []
lista_sheldon = []

# Función para calcular si un número es primo
def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True

# Función para calcular el producto de los dígitos de un número
def m(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

# Función para calcular el número espejo de un número       
def r(number):
    return int(str(number)[::-1])

# Función para generar una lista de números primos
def generar_lista_primos(start = 2 ,  end = 100 ):
    #primos.append(1)
    for i in range(start, end):
        if is_prime(i):
            primos.append(i)
    return primos

# Función para verificar si un número es espejo
def verificarNumeroEspejo(number):
    #print(number)
    rNumber = r(number)
    posMirror = r(primos.index(rNumber) + 1)
    return primos[posMirror - 1] == number


def generarSheldonNumbers (start = 0 , end = 100):
    for i in range(start,end):
        if verificarNumeroSheldon(i):
            lista_sheldon.append(i)

    return lista_sheldon



# Función para verificar si un número cumple las 3 condiciones de la conjetura de Sheldon
def verificarNumeroSheldon(number):
    primeraCondicion = segundaCondicion = terceraCondicion = False

    # # this works
    # if (is_prime(number)): 
    #     print("El número {} es primo".format(number))
    #     primeraCondicion = True

    # # this also works
    # if (m(number) == primos.index(number) + 1):         
    #     print("El producto de sus dígitos ({}) es igual a su posición en la lista de todos los primos ({})".format(m(number), primos.index(number) + 1))
    #     segundaCondicion = True
    # else:
    #     print("El producto de sus dígitos ({}) NO es igual a su posición en la lista de todos los primos ({})".format(m(number), primos.index(number) + 1))       
    
    # terceraCondicion = verificarNumeroEspejo(number)

    if (is_prime(number) and m(number) == primos.index(number) + 1 and verificarNumeroEspejo(number)): 
        #print("El número {} cumple las 3 condiciones".format(number))
        return True
    # cumple las 3 condiciones
    # if primeraCondicion and segundaCondicion and terceraCondicion:      
    #     return True    
    return False



generar_lista_primos(end = 100000)

print(primos)

# # caso específico
# if verificarNumeroSheldon(73): 
#     print("El número 73 cumple la conjetura de Sheldon")
# else:
#     print("El número 73 NO cumple la conjetura de Sheldon")

# caso general
lista = generarSheldonNumbers (end = 100000)
print (lista)
#verificarNumeroSheldon(73)

#print(lista)


