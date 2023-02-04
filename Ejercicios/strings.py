def concatenar(first_name, last_name):
    return first_name + " " + last_name

def longitud(texto):
    return len(texto)

def palindromo(texto):
    if texto == texto[::-1]:
        return("Es un palindromo")
    else:
        return("No es un palindromo")



cadena = input("Ingrese un texto: ")
print ("La longitud de la cadena es: " ,longitud(cadena))
# print (concatenar("jorge", "barquero"))