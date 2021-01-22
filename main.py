x = input("Whats your first name?")
u = input("Whats your last name?")
print("I like that name")
print("Hi "+ x + u)
t = input("Hows your day been?(All lowercase)")
if((t == "great")):
  print("Thats great to hear")
if((t == "good")):
    print("Thats great to hear")
else:
  print("Thats sucks")
  #fix the colors error 1/20/21- done 1/20/21
q = input("Whats your favorite color?(All lowercase)")
if((q == "green")):
  print("Thats my favorite color as well!")
if((q == "black")):
  print("Thats my favorite color!")
if((q == "red")):
  print("Thats my favorite color!")
else: 
  print("Thats a nice color but its not my favorit one")
w = input("How many pets do you have?")
print("Cool!! I have")
from random import randint
#take seed out
for _ in range(1):
	value = randint(0,10)
	print(value)


print("Its been great getting to know you!")