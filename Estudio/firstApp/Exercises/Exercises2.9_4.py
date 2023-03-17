# Create a function to convert from Celsius degrees to Fahrenheit degrees
# Formula: F  = C * 1.8 + 32
def askTemperature():
    celsius: float = input("Celsius degrees: ")
    return convert(float(celsius))


def convert (celsius: float):
    fahrenheit = celsius * 1.8 + 32
    print("Fahrenheit degrees: {0}".format(fahrenheit))
    

askTemperature()
