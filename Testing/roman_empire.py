import random
class Country():
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

def main():
    current_country = 0
    alive = True
    countries = []
    print("Welcome player. You will be playing as Julius Caesar as he travels across his empire.")
    rome_italy = Country("You are currently stationed in the marvelous capital of the Roman Empire. Large columned"
                         " buildings are all around you.", 2, 1, None, None)
    countries.append(rome_italy)
    naples_italy = Country("You are currently visiting the cultural heart of the southern tip of the Roman Empire. "
                           "here you will see marble statues of yourself", 0, None, None, None)
    countries.append(naples_italy)
    venice_italy = Country(
        "You are entering venice. There was an attempt on your life, but your guards subdued the "
        "threat.", 4, None, 3, 8)
    countries.append(venice_italy)

    sarajevo_italy = Country("You are entering a highly contentious area. Most of the locals would like to see the "
                             "empire of Rome fall.", 3, 5, None, 2)
    countries.append(sarajevo_italy)

    zurich_switzerland = Country("You are entering the border between the empire and Germania. The Germanic tribes"
                                 " have been committing border skirmishes alongside the outskirts of zurich", 6, 2,
                                 None, None)
    countries.append(zurich_switzerland)

    athens_greece = Country("Welcome to the birthplace of democratic and republican ideals. \nAthens was once the site"
                            " of a powerful democratic state. However wars with Sparta and the Macedonians, left "
                            "Athens in ruins.", 3, None, None, None)
    countries.append(athens_greece)

    munich_germany = Country("You have started an invasion of the Germanic homeland.\nYou don't have enough manpower or"
                             " supplies to supply an invasion of this scale. Turn back", 7, 4, None, None)
    countries.append(munich_germany)

    germania_germany = Country("Surprisingly; you been able to make a mad dash towards the capital of the germanic"
                               " tribes.\n However their military has noticed you and its only matter of time"
                               " until they destroy your army.", None, 6, None, None)
    countries.append(germania_germany)

    paris_france = Country("you have entered recently conquered territory.", None, 9, 7, None)
    countries.append(paris_france)

    madrid_spain = Country("you are entering the beautiful countryside of Hispania. Here you will see remnants of the"
                           "once powerful Carthaginian empire.", 8, None, None, None)
    countries.append(madrid_spain)

    while alive is not False:
        print(countries[current_country].description)
        caesar_choice = input("which direction would you like to go? ")

        if caesar_choice.lower() == "north" or caesar_choice.lower() == "n":
            next_country = countries[current_country].north
            if countries[current_country].north is None:
                print("you cant go that way")
            else:
                current_country = next_country

        elif caesar_choice.lower() == "south" or caesar_choice.lower() == "s":
            next_country = countries[current_country].south
            if countries[current_country].south is None:
                print("you cant go that way")
            else:
                current_country = next_country

        elif caesar_choice.lower() == "east" or caesar_choice.lower() == "e":
            next_country = countries[current_country].east
            if countries[current_country].east is None:
                print("you cant go that way")
            else:
                current_country = next_country
        elif caesar_choice.lower() == "west" or caesar_choice.lower() == "w":
            next_country = countries[current_country].west
            if countries[current_country].west is None:
                print("you cant go that way")
            else:
                current_country = next_country
        else:
            print("YOU FUCKING DONKEH!!!")

        print()

main()