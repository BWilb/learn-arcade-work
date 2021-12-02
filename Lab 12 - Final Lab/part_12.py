import random
import Germans
import RomanSoldier
import RomanCitizens

"""For my final project, I am creating a mashup of a text adventure and sprite game. """

class Julius_Caesar:
    """This class represents Julius Caesar"""
    def __init__(self):
        self.health = 100
        # Character's health
        self.energy = 100
        # Character's awareness
        self.hunger = 0
        # Character's hunger levels
        self.thirst = 0
        # Character's thirst levels
        self.inventory = None
        # Character's inventory
        self.army_list = None
        # Character's army inventory

class Locations:
    def __init__(self, north, east, south, west):
        self.description = None
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def locations():
    locations = []
    berlin_germany = Locations(None, None, 1, None)
    berlin_germany.description = "Known for being the most militarily powerful city amongst the tribes of Germania, " \
                                 "it was an impressive feat that you were able to sack it.\nHowever it cost you your " \
                                 "legions. Get out before you and your remaining soldiers are killed. " \
                                 "Go south to Munich."
    locations.append(berlin_germany)

    munich_germany = Locations(0, None, 2, 9)
    munich_germany.description = "Welcome to the heart of Germania's economic activity. Sacking this city would truly "\
                                 "cripple german war support.\n You can move west to reach Alsaice-Lorraine, "\
                                 "south to Zurich, or north to Berlin"
    locations.append(munich_germany)

    zurich_switzerland = Locations(1, 3, 5, None)
    zurich_switzerland.description = "Ah...the land of peace and chocolate. At least in Zurich, you can't get harmed by"\
                                     " barbarians if you're considered a traveller \nbut your citizens will be. " \
                                     "Go south to Rome, go north to Munich, go east to Vienna"
    locations.append(zurich_switzerland)

    venice_rome = Locations(2, 9, 6, 5)
    venice_rome.description = "Venice. Rome's most important city of all, besides Rome itself. \n" \
                              "being the economic hub that it is, we definitely would not want it to fall into " \
                              "enemy hands. Go west to Genoa, east to Vienna, south to Rome, north to Zurich"
    locations.append(venice_rome)

    genoa_rome = Locations(None, 3, None, None)
    genoa_rome.description = "Welcome to Genoa. Most of our finest sailors and merchants come from this city. Go east" \
                             " to Zurich"
    locations.append(genoa_rome)

    rome_rome = Locations(2, None, 10, None)
    rome_rome.description = "Rome. Look at her splendor. The marble white columns, the paved roads, the Colosseum \n" \
                            "we definitely wouldn't want this city to come under fire. Go south to Naples or go " \
                            "North to Zurich."
    locations.append(rome_rome)

    vienna_germany = Locations(None, 7, None, 2)
    vienna_germany.description = "Ah...Vienna, a sacred place of battle for the Romans. This where " \
                                 "we first defeated the Germanic barbarians.\nNow the city lies smoldering. Go east to"\
                                 " Budapest or go west to Zurich."
    locations.append(vienna_germany)

    budapest_hun = Locations(None, None, 8, 6)
    budapest_hun.description = "No time to explain, Budapest Hungary is full of dangerous Huns. Get out before we are" \
                               " spotted! Go west to Vienna. Go south to Belgrade"
    locations.append(budapest_hun)

    belgrade_serb = Locations(7, None, None, None)
    belgrade_serb.description = "Rome has not yet conquered Belgrade, but the Almighty Caesar knows his next target. \n"\
                                "Go north to Budapest"
    locations.append(belgrade_serb)

    alsaice_france = Locations(None, 1, None, None)
    alsaice_france.description = "Alsaice Gaul. Rome knows nothing about this territory. Go east to Berlin"
    locations.append(alsaice_france)

    naples_rome = Locations(5, None, None, None)
    naples_rome.description = "Congrats, you've made it back to Naples, possibly unscathed or not. Go back and kick the" \
                              " Germans from Rome's soil."
    locations.append(naples_rome)
    return locations

def main():
    total_miles_travelled = 0
    barbarian_distance = -15
    choices = ["Move",
               "Stop and rest",
               "Eat",
               "Drink",
               "View Map"]
    # Choices that Caesar has

    directions = ["\nNorth",
                  "South",
                  "East",
                  "West\n"]

    german_warriors = [100]
    for i in range(len(german_warriors)):
        german_warriors[i] = Germans.Germans()
        # Creation of 100 German opponents

    roman_soldiers = [200]
    for i in range(len(roman_soldiers)):
        roman_soldiers[i] = RomanSoldier.Roman_Soldier()
        # Creation of 200 Roman soldiers

    roman_citizens = [15000]
    for i in range(len(roman_citizens)):
        roman_citizens[i] = RomanCitizens.RomanCitizens()
        # Creation of 15000 Roman civilians

    caesar = Julius_Caesar()
    current_country = 0
    alive = True
    countries = locations()

    print("Welcome player. You will be playing as Julius Caesar. You are currently in the territory of the barbaric"
          " German tribes.\nYou've recently scored a major victory against the Germans, however your legions were "
          "desimiated.\nYou are to return to Naples Rome, all the while; gathering more troops and supplies along the way."
          "\nYou will be able to sight see many of the cities Rome has conquered or will conquer, but be warned"
          "the Germans are regathering their own army.\nTry to avoid contact at all costs and return to Naples as quickly"
          " as possible, since they are after Roman wealth as well.\n")


    while alive is not False:
        print(countries[current_country].description)
        for i in range(len(choices)):
            print(choices[i])
        caesar_choice = input("\nWhat would you like to do?: ")

        if caesar_choice.lower() == "move" or caesar_choice.lower() == "m":
            """"""
            caesar.energy -= random.randrange()
            for i in range(len(directions)):
                print(directions[i])
            direction = input("Which direction would you like to move?: ")
            if direction.lower() == "north" or direction.lower() == "n":
                next_country = countries[current_country].north
                if countries[current_country].north is None:
                    print("you cant go that way")
                else:
                    current_country = next_country

            elif direction.lower() == "south" or direction.lower() == "s":
                next_country = countries[current_country].south
                if countries[current_country].south is None:
                    print("you cant go that way")
                else:
                    current_country = next_country

            elif direction.lower() == "east" or direction.lower() == "e":
                next_country = countries[current_country].east
                if countries[current_country].east is None:
                    print("you cant go that way")
                else:
                    current_country = next_country
            elif direction.lower() == "west" or direction.lower() == "w":
                next_country = countries[current_country].west
                if countries[current_country].west is None:
                    print("you cant go that way")
                else:
                    current_country = next_country
            else:
                print("I am sorry, that option is not available. Try again, but remember the Germans are currently hunting "
                      "you down.")

        print()

main()
"""country = []
for countries in range(len(LocationDescriptions.locations())):
    country.append(LocationDescriptions.locations()[countries].description)

print(country[1])"""