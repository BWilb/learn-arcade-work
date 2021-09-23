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
    function. I have also created a couple unique random events besides finding an oasis.
    I have also included line breaks on the choices, so that the code looks cleaner"""
    miles_travelled = 0
    thirst = 0
    total_miles = 200
    canteen_drinks = 5
    owner_miles = -20
    camel_tired = 0
    done = False

    description()

    while not done:
        print("\nA. Drink from your canteen")
        print("B. Ahead moderate speed")
        print("C. Ahead full speed")
        print("D. Stop for the night")
        print("E. Status check")
        print("Q. Quit \n")

        choice = input("What is your decision? ")

        if choice.lower() == "q":
            # This section of code is for quitting
            print("Good choice to quit the game. Bye.")
            done = True

        elif choice.lower() == "e":
            # This section of code is for checking your status
            print(f"You have travelled {miles_travelled} miles")
            print(f"You have {canteen_drinks} drinks left")
            print(f"The natives are {miles_travelled - owner_miles} miles behind you")

        elif choice.lower() == "d":
            # This entire section of code is for stopping for the night
            camel_tired = 0
            print("Your stolen camel is happy")
            owner_miles += random.randrange(7, 14)

        elif choice.lower() == "c":
            # this entire section of code for option c is for extreme speed
            miles_travelled += random.randrange(10, 20)
            camel_tired += random.randrange(1, 3)
            owner_miles += random.randrange(7, 14)

        elif choice.lower() == "b":
            # This entire section of code is for moderate speed
            miles_travelled += random.randrange(5, 12)
            camel_tired += 1
            owner_miles += random.randrange(7, 14)

        elif choice.lower() == "a":
            # This section of code is for drinking from canteen
            if canteen_drinks > 0:
                canteen_drinks -= 1
                print(f"You have {canteen_drinks} drinks left")
                thirst = 0
            else:
                print("You dont have any drinks left in your canteen! Good luck!")

        print(f"You have travelled {miles_travelled} miles")
        if miles_travelled >= total_miles:
            print("You have escaped your consequences and won the game!")
            break
        thirst += 1
        if thirst >= 6:
            print("You have died of thirst. Goodbye")
            done = True
        elif thirst >= 4:
            print("You are a thirsty boy. Drink some water")
        if camel_tired >= 8:
            print("Your camel died and you lost the game")
            done = True
        elif camel_tired >= 5:
            print("Your camel is getting tired. You better get some rest")
        if owner_miles >= miles_travelled:
            print("The natives have caught you")
            done = True
        elif owner_miles < miles_travelled:
            if miles_travelled - owner_miles <= 15:
                print("The owners are close behind you")
        if miles_travelled % 20 == 1:
            print("You have found an oasis")
            camel_tired = 0
            thirst = 0
            canteen_drinks = 5
        if miles_travelled % 50 == 1:
            stole = random.randrange(1, 5)
            canteen_drinks -= stole
            print(f"A desert wanderer has stolen {stole} of your drinks")
        if miles_travelled % 75 == 0:
            print("Your camel has died due to stress and you've been captured")
            done = True

main()