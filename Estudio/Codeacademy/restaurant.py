# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage","olives", "anchovies","mushrooms"]
price = [2,6,1,3,2,7,2]
num_two_dollar_slices = price.count(2)
#print (num_two_dollar_slices)

num_pizzas = len(toppings)
#print(num_pizzas)

print ("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

pizza_and_prices.sort()
print (pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
print ("Cheapest: " + str(cheapest_pizza))

priciest_pizza = pizza_and_prices[-1]
print ("Priciest:" + str(priciest_pizza))
#vender la ultima pizza
pizza_and_prices.pop(-1)
print (pizza_and_prices)

#agregar nueva pizza
pizza_and_prices.insert(4, [2.5, "peppers"])
print (pizza_and_prices)


three_cheapest = pizza_and_prices[:3]

print ("Three cheapest: "+ str(three_cheapest))

