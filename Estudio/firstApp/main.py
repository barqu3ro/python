def say_hello(x: str, y: str):
    print("Hello {0}, you are {1}".format(x, y))
    # print("TEST")


def double_number(number: int):
    return number * 2


def print_double_number(number: int):
    result = double_number(number)
    print("Double of your age (" + str(number) + ") is " + str(result))


# Ask user name
user_name: str = input("What is your name? ")
# Ask user age
user_age: int = input("How old are you? ")
say_hello(user_name, str(user_age))
print_double_number(int(user_age))
