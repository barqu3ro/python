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



primos = []

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


# Main program
def Main():
    primos = []

    # Calcular los primos entre 1 y 1.000.000
    for i in range(1, 1000000):
        if is_prime(i):
            primos.append(i)    # aquí agrego el número primo a la lista de primos para validar la primera condición


    # Calcular los números de Sheldon
    for i in primos:
        # aquí quedé me voy a dormir 
        


