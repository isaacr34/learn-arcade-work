import random

print("Welcome to Camel!")
print("You have stolen a camel tto make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and outrun the natives.")
print()

done = False
distance = 0
natives = -20
tiredness = 0
canteen = 3

while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop and rest.")
    print("E. Status check.")
    print("Q. Quit.")
    print("Your choice? ")

    userInput = input("Your choice? ")

    if userInput.lower() == "q":
        done = True
