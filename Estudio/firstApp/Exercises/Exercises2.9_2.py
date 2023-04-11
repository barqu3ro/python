def ask_numbers():
    firstNumber: int = input("First number: ")
    secondNumber: int = input("Second number: ")
    sumNumbers(int(firstNumber), int(secondNumber))


def sumNumbers(firstNumber: int, secondNumber: int):
    suma =  firstNumber + secondNumber
    print(suma)


ask_numbers()
