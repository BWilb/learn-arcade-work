correct_num = 17

print("""Hello...user, you wanna play a little game.
I've come up with a random number, that you have to guess.
If you do not guess the correct number after 10 tries you die!!!!""")

i = 0
while(i < 10):
    guessed_num = input("enter a number, this is your " + str(i + 1) + " try")
    if(guessed_num < correct_num):
        print("your number is too low, guess again")
    elif(guessed_num > correct_num):
        print("your number is too high, guess again")
    elif(guessed_num == correct_num):
        print("you guessed correctly")
        break
i += 1