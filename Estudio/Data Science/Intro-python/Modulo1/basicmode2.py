# Crear un programa que devuelva el septuagésimo tercer número de fibonnacci

def specific_fibonacci (number):
    x = 0
    y = 1
    fib_list = [0,1]    
    if number <= 0 :
        return x
    elif number == 1:
        return y
    else:
        for _ in range(number-2):
            fib_list.append(x + y)
            x = y 
            y = fib_list[-1]

    print (fib_list)

    return fib_list[-1]


inputNumber = int(input('Indica el número a generar: '))

print ('El número {} de la serie fibonacci es {}'.format(inputNumber, specific_fibonacci(inputNumber)))