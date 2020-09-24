import random


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel tto make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and outrun the natives.")
    print()

    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    miles_natives = -20
    canteen = 3

    while not done:
        print()
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop and rest.")
        print("E. Status check.")
        print("Q. Quit.")

        user_input = input("Your choice? ")
        print()

        if user_input.upper() == "Q":
            done = True
            print("Quitter")
        elif user_input.upper() == "E":
            print("Miles traveled: " + str(miles_traveled))
            print("Drinks in canteen: " + str(canteen))
            print(f"The natives are {miles_traveled - miles_natives} miles behind you.")
        elif user_input.upper() == "D":
            n_miles = random.randrange(7, 14)
            camel_tiredness = 0
            print("The camel is happy!")
            miles_natives += n_miles
            print(f"The natives traveled {n_miles} miles")
        elif user_input.upper() == "C":
            miles = random.randrange(10, 20)
            n_miles = random.randrange(7, 14)
            thirst += 1
            camel_tiredness += random.randrange(1, 3)
            miles_traveled += miles
            miles_natives += n_miles
            oasis = random.randrange(20)
            if oasis == 7:
                thirst = 0
                camel_tiredness = 0
                canteen = 3
                print("As you were traveling you found an oasis!")
                print("You and your camel drink and rest.")
            else:
                print(f"You traveled {miles} miles.")
                print(f"The natives traveled {n_miles} miles.")
        elif user_input.upper() == "B":
            miles = random.randrange(5, 12)
            n_miles = random.randrange(7, 14)
            thirst += 1
            camel_tiredness += 1
            miles_traveled += miles
            miles_natives += n_miles
            oasis = random.randrange(20)
            if oasis == 7:
                thirst = 0
                camel_tiredness = 0
                canteen = 3
                print("As you were traveling you found an oasis!")
                print("You and your camel drink and rest.")
            else:
                print(f"You traveled {miles} miles.")
                print(f"The natives traveled {n_miles} miles.")
        elif user_input.upper() == "A":
            if canteen > 0:
                print("You take a drink from your canteen.")
                canteen -= 1
                thirst = 0
            elif canteen == 0:
                print("There is no water in your canteen.")
        if not done and 7 > thirst > 4:
            print("You are thirsty.")
        if thirst > 6:
            print("You died of thirst!")
            done = True
        if not done and 9 > camel_tiredness > 5:
            print("Your camel is getting tired.")
        if camel_tiredness > 8:
            print("Your camel is dead.")
            done = True
        if not done and miles_natives >= miles_traveled:
            print("The natives have caught you!")
            done = True
        elif (miles_traveled - miles_natives) <= 15:
            print("The natives are getting close!")
        if miles_traveled >= 200:
            print("You have made it across the Mobi desert and survived!")
            done = True


main()
