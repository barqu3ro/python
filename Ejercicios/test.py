class Concatenador:
    def concatenar_strings(self, string1, string2):
        return string1 + string2
    
    def sumar_numeros(self, num1, num2):
        return num1 + num2

concatenador = Concatenador()
string_result = concatenador.concatenar_strings("Hola", " mundo")
print("Resultado de la concatenación de strings:", string_result)

num_result = concatenador.sumar_numeros(5, 3)
print("Resultado de la suma de números:", num_result)
