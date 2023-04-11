import random

name = "Pablo"
question = ""
answer = ""

random_number = random.randint(1, 11)

if name == "" :
  print("Question: "+ question)
else: 
  print (name + " asks: " + question)
#print (random_number)




if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Nothing here"
elif random_number == 11:
  answer = "You'll die soon"
else:
  print ("Error")

if question == "":
  print ("Error - Not question given")
else:
  print ("Magic 8-ball's answer: " + answer)