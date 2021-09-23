import random

def description():
    """I wanted to make my main function a little shorter, so I
    placed the game description in a different function"""

    print("Welcome to the ever so popular game of Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print("They are mad and want you to pay for your crimes.")
    print("Survive your 200 mile desert trek and out run the natives.")

def main():
    """This is the main function
    I have my variables declared, then I call the game description
    function"""
    miles_travelled = 0
    thirst = 0
    total_miles = 200
    canteen_drinks = 5
    owner_miles = -20
    camel_tired = 0
    done = False

    description()

    #I included line breaks into the specific options, so that it would look a lot cleaner
    while not done:
        print("\nA. Drink from your canteen")
        print("B. Ahead moderate speed")
        print("C. Ahead full speed")
        print("D. Stop for the night")
        print("E. Status check")
        print("Q. Quit \n" )

        choice = input("What is your decision? ")

        #This section of code is for quitting
        if choice.lower() == "q":
            print("Good choice to quit the game. Bye.")
            done = True

        #This section of code is for checking your status
        elif choice.lower() == "e":
            print(f"You have travelled {miles_travelled} miles")
            print(f"You have {canteen_drinks} drinks left")
            print(f"The natives are {miles_travelled - owner_miles} miles behind you")

        #This entire section of code is for stopping for the night
        elif choice.lower() == "d":
            camel_tired = 0
            print("Your stolen camel is happy")
            owner_miles += random.randrange(7, 14)
            if owner_miles >= miles_travelled:
                print("The natives have caught you")
                done = True
            elif owner_miles < miles_travelled:
                if miles_travelled - owner_miles <= 15:
                    print("The owners are close behind you")

        #this entire section of code for option c is for extreme speed
        elif choice.lower() == "c":
            miles_travelled += random.randrange(10, 20)
            print(f"You have travelled {miles_travelled} miles")
            if miles_travelled >= total_miles:
                print("You have escaped your consequences and won the game!")
                break
            if miles_travelled % 20 == 0:
                print("You have found an oasis")
                camel_tired = 0
                thirst = 0
                canteen_drinks = 5
            if miles_travelled % 50 == 0:
                stole = random.randrange(1, 5)
                canteen_drinks -= stole
                print(f"A desert wanderer has stolen {stole} of your drinks")
            if miles_travelled % 75 == 0:
                print("Your camel has died due to stress and you've been captured")
                done = True
            thirst += 1
            if thirst > 4:
                print("You are a thirsty boy. Drink some water")
            elif thirst > 6:
                print("You have died of thirst. Goodbye")
                done = True
            camel_tired += random.randrange(1, 3)
            if camel_tired > 5:
                print("Your camel is getting tired. You better get some rest")
            elif camel_tired > 8:
                print("Your camel died and you lost the game")
                done = True
            owner_miles += random.randrange(7, 14)
            if owner_miles >= miles_travelled:
                print("The natives have caught you")
                done = True
            elif owner_miles < miles_travelled:
                if miles_travelled - owner_miles <= 15:
                    print("The owners are close behind you")

        #This entire section of code is for moderate speed
        elif choice.lower() == "b":
            miles_travelled += random.randrange(5, 12)
            print(f"You have travelled {miles_travelled} miles")
            if miles_travelled >= total_miles:
                print("You have escaped your consequences and won the game!")
                break
            if miles_travelled % 20 == 0:
                print("You have found an oasis")
                camel_tired = 0
                thirst = 0
                canteen_drinks = 5
            if miles_travelled % 50 == 0:
                stole = random.randrange(1, 5)
                canteen_drinks -= stole
                print(f"A desert wanderer has stolen {stole} of your drinks")
            if miles_travelled % 75 == 0:
                print("Your camel has died due to stress and you've been captured")
                done = True
            thirst += 1
            if thirst > 4:
                print("You are a thirsty boy. Drink some water")
            elif thirst > 6:
                print("You have died of thirst. Goodbye")
                done = True
            camel_tired += 1
            if camel_tired > 5:
                print("Your camel is getting tired. You better get some rest")
            elif camel_tired > 8:
                print("Your camel died and you lost the game")
                done = True
            owner_miles += random.randrange(7, 14)
            if owner_miles >= miles_travelled:
                print("The natives have caught you")
                done = True
            elif owner_miles < miles_travelled:
                if miles_travelled - owner_miles <= 15:
                    print("The owners are close behind you")

        #this section of code is for drinking from canteen
        elif choice.lower() == "a":
            if canteen_drinks > 0:
                canteen_drinks -= 1
                print(f"You have {canteen_drinks} drinks left")
                thirst = 0
            else:
                print("You dont have any drinks left in your canteen! Good luck!")
main()