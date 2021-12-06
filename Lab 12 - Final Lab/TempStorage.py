try:
    caesar_choice = int(input("\nWhat would you like to do?: "))

    if caesar_choice == 1 or caesar_choice == 1:
        """Through moving, Caesar loses energy and gains hunger and thirst.
        Since there are Germans everywhere, even in Rome's territory
        , Caesar is also most likely going to run into some.
        """
        caesar.energy -= random.randrange(1, 50)
        caesar.hunger += random.randrange(1, 5)
        caesar.thirst += random.randrange(1, 5)

        for i in range(len(directions)):
            print(directions[i])
        direction = input("Which direction would you like to move?: ")
        if direction.lower() == "north" or direction.lower() == "n":
            # If statement that determines where you go, when you select direction
            next_country = major_cities[current_country].north
            if major_cities[current_country].north is None:
                print("you cant go that way")
            else:
                current_country = next_country
                total_miles_travelled += random.randrange(1, 400)

        if direction.lower() == "north east" or direction.lower() == "ne":
            # If statement that determines where you go, when you select direction
            next_country = major_cities[current_country].north_east
            if major_cities[current_country].north_east is None:
                print("you cant go that way")
            else:
                current_country = next_country
                total_miles_travelled += random.randrange(1, 400)

        if direction.lower() == "north west" or direction.lower() == "nw":
            # If statement that determines where you go, when you select direction
            next_country = major_cities[current_country].north_west
            if major_cities[current_country].north_west is None:
                print("you cant go that way")
            else:
                current_country = next_country
                total_miles_travelled += random.randrange(1, 400)

        elif direction.lower() == "south" or direction.lower() == "s":
            next_country = major_cities[current_country].south
            if major_cities[current_country].south is None:
                print("you cant go that way")
            else:
                current_country = next_country
                total_miles_travelled += random.randrange(1, 400)

        elif direction.lower() == "south east" or direction.lower() == "se":
            next_country = major_cities[current_country].south_east
            if major_cities[current_country].south_east is None:
                print("you cant go that way")
            else:
                current_country = next_country
                total_miles_travelled += random.randrange(1, 400)

        elif direction.lower() == "south west" or direction.lower() == "sw":
            next_country = major_cities[current_country].south_west
            if major_cities[current_country].south_west is None:
                print("you cant go that way")
            else:
                current_country = next_country
                total_miles_travelled += random.randrange(1, 400)

        elif direction.lower() == "east" or direction.lower() == "e":
            next_country = major_cities[current_country].east
            if major_cities[current_country].east is None:
                print("you cant go that way")
            else:
                current_country = next_country
                total_miles_travelled += random.randrange(1, 400)

        elif direction.lower() == "west" or direction.lower() == "w":
            next_country = major_cities[current_country].west
            if major_cities[current_country].west is None:
                print("you cant go that way")
            else:
                current_country = next_country
                total_miles_travelled += random.randrange(1, 400)
        else:
            print("I don't understand what you mean?")

    elif caesar_choice == 2 or caesar_choice == 2:
        # If statement if user chooses to rest
        caesar.health = 100
        for i in range(len(roman_soldiers)):
            roman_soldiers[i].health = 50
        print("Congrats. You and your army have rested up")

    elif caesar_choice == 3 or caesar_choice == 3:
        caesar.hunger = 0
        caesar.energy += random.randrange(1, 10)
        caesar.health += 10
        """binary search through supplies list"""
        key = "food"
        found = False
        lower_bound = 0
        upper_bound = len(supplies_list) - 1
        while lower_bound <= upper_bound:
            middle_pos = (lower_bound + upper_bound) // 2
            if supplies_list[middle_pos] < key:
                lower_bound = middle_pos + 1
            elif supplies_list[middle_pos] > key:
                upper_bound = middle_pos - 1
            else:
                found = True
                supplies_list.remove(supplies_list[middle_pos])
                break
        print("you chose to eat")

    elif caesar_choice == 4 or caesar_choice == 4:
        # If statement if user chooses to eat
        caesar.thirst = 0
        caesar.energy += random.randrange(1, 5)
        caesar.health += 4

        key = "water"
        found = False
        lower_bound = 0
        upper_bound = len(supplies_list) - 1
        while lower_bound <= upper_bound:
            middle_pos = (lower_bound + upper_bound) // 2
            if supplies_list[middle_pos] < key:
                lower_bound = middle_pos + 1
            elif supplies_list[middle_pos] > key:
                upper_bound = middle_pos - 1
            else:
                found = True
                supplies_list.remove(supplies_list[middle_pos])
                break

        print("you chose to drink")

    # elif caesar_choice.lower() == "view map" or caesar_choice.lower() == "v":
    # If statement that shows user where they are

    elif caesar_choice == 6 or caesar_choice == 6:
        # If function that closes game if user chooses to
        print("good choice\n"
              "goodbye")
        break

    elif caesar_choice == 7 or caesar_choice == 7:
        # If function that shows player their stats
        print(f"your energy levels are {caesar.energy}")
        print(f"you have {caesar.health} health pts")
        print(f"you have {caesar.thirst} thirst pts")
        print(f"you have {caesar.hunger} hunger pts")
        print(f"you have {len(roman_soldiers)} soldiers left")
        print(f"There are {len(roman_citizens)} citizens left")
        for food in range(len(supplies_list)):
            print(f"{food + 1}", supplies_list[food])

    else:
        print("I'm sorry that option is not available. Just remember there are Germans everywhere, who are after"
              " you and your people.\nYou better hurry up.")
except:
    print("You are supposed to insert the specific number to choice")