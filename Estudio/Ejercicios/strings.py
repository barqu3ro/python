def concatenar(first_name, last_name):
    return first_name + " " + last_name

def longitud(texto):
    return len(texto)

def is_palindromo(texto):    
    if texto == texto[::-1]:
        return("Es un palindromo")
    else:
        return("No es un palindromo")

def is_palindromo_plain(text):
    return text == text[::-1]




cadena = input("Ingrese un texto: ")
print ("La longitud de la cadena es: " ,longitud(cadena))
# print (concatenar("jorge", "barquero"))

# textoPalindromo = input("Ingrese un texto para verificar si es palindromo: ")
textoPalindromo = "anita lava la tina"
print("El texto " , textoPalindromo , is_palindromo(textoPalindromo))


frase = "anita lava la tina"
print(is_palindromo_plain(frase))

