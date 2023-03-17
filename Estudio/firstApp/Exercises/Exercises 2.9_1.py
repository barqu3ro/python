def ask_info():
    name: str = input("What is your name? ")
    age: int = input("What is your age? ")
    print_info(str(name), str(age))


def print_info(name:str, age:str):
    print("Hello {0}, you are {1}".format(name, age))
    
    
ask_info()