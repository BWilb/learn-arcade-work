import random
import German
import RomanSoldier
import RomanCitizen

"""For my final project, I am creating a mashup of a text adventure and sprite game. """

class JuliusCaesar:
    # This class represents Julius Caesar
    def __init__(self):
        self.health = 200
        # Character's health
        self.energy = 100
        # Character's awareness
        self.hunger = 0
        # Character's hunger levels
        self.thirst = 0
        # Character's thirst level
        self.troop_loss = 0
        # Caesar's troop loss
        self.civilian_loss = 0
        # Caesar's civilian loss
        self.score_card = 0
        # Caesar's german kill count

class Locations:
    def __init__(self, north, north_east, north_west, east, south, south_east, south_west, west):
        self.description = None
        self.north = north
        self.north_east = north_east
        self.north_west = north_west
        self.east = east
        self.south = south
        self.south_east = south_east
        self.south_west = south_west
        self.west = west

def locations():
    locations = []
    """German villages"""
    berlin_germany = Locations(None, None, None, None, 1, None, 8, None)
    berlin_germany.description = "Known for being the most militarily powerful city amongst the tribes of Germania, " \
                                 "it was an impressive feat that you were able to sack it.\nHowever it cost you your " \
                                 "legions. Get out before you and your remaining soldiers are killed. " \
                                 "Go south to Munich. Go south west to Alsace-Lorraine\n"
    locations.append(berlin_germany)

    munich_germany = Locations(0, None, 81, None, 3, None, None, None)
    munich_germany.description = "Welcome to the heart of Germania's economic activity...Munich. Sacking this city would truly "\
                                 "cripple german war support.\nYou can move north west to reach Alsace-Lorraine, "\
                                 "south to Zurich, or north to Berlin\n"
    locations.append(munich_germany)

    vienna_germany = Locations(None, None, None, 9, None, 10, 4, 3)
    vienna_germany.description = "Ah...Vienna, a sacred place of battle for the Romans. This where " \
                                 "we first defeated the Germanic barbarians.\nNow the city lies smoldering. Go east to" \
                                 " Budapest, go west to Zurich, go south east to Belgrade, or go south west to Venice\n"
    locations.append(vienna_germany)

    zurich_switzerland = Locations(None, 1, None, 2, None, 4, None, None)
    zurich_switzerland.description = "Ah...the land of peace and chocolate. At least in Zurich, you can't get harmed by"\
                                     " barbarians if you're considered a traveller\nbut your citizens will be. " \
                                     "Go south east to Venice, go north east to Munich, go east to Vienna\n"
    locations.append(zurich_switzerland)

    """Roman cities"""
    venice_rome = Locations(1, 2, 3, None, None, None, 6, 5)
    venice_rome.description = "Venice. Rome's most important city of all, besides Rome itself. \n" \
                              "being the economic hub that it is, we definitely would not want it to fall into " \
                              "enemy hands. Go west to Genoa, north to Munich," \
                              " north east to Vienna, south west to Rome, north west to Zurich\n"
    locations.append(venice_rome)

    genoa_rome = Locations(3, 1, None, 5, None, None, None, None)
    genoa_rome.description = "Welcome to Genoa. Most of our finest sailors and merchants come from this city. Go east" \
                             " to Venice or north to Zurich, or north east to Munich\n"
    locations.append(genoa_rome)

    rome_rome = Locations(None, 5, None, None, None, 7, None, None)
    rome_rome.description = "Rome. Look at her splendor. The marble white columns, the paved roads, the Colosseum\n" \
                            "we definitely wouldn't want this city to come under fire. Go south east to Naples or go " \
                            "north east to Venice.\n"
    locations.append(rome_rome)

    naples_rome = Locations(None, None, None, None, None, None, None, None)
    naples_rome.description = "Congrats, you've made it back to Naples, possibly unscathed or not. Go back and kick the" \
                              " Germans from Rome's soil.\n"
    locations.append(naples_rome)

    """Other important cities"""
    alsace_france = Locations(None, 0, None, None, None, 1, None, None)
    alsace_france.description = "Alsace Gaul. Rome knows nothing about this territory. Go north east to Berlin " \
                                "or go south east to Munich.\n"
    locations.append(alsace_france)

    budapest_hun = Locations(None, None, 2, None, 10, None, None, None)
    budapest_hun.description = "No time to explain, Budapest Hungary is full of dangerous Huns. Get out before we are" \
                               " spotted! Go north west to Vienna. Go south to Belgrade\n"
    locations.append(budapest_hun)

    belgrade_serb = Locations(9, None, 2, None, None, 11, None, None)
    belgrade_serb.description = "Rome has not yet conquered Belgrade, but the Almighty Caesar knows his next target.\n" \
                                "Go north to Budapest, north west to Vienna, or south east to Athens.\n"
    locations.append(belgrade_serb)

    """Greek Cities"""
    athens_greece = Locations(None, 10, None, None, None, 12, None, None)
    athens_greece.description = "Athens Greece...the birth place of democracy and Plato's Republic. I shall implement ideals" \
                                " that once flowed through this very city once I return to Rome.\n" \
                                "Go north east to Belgrade, go south east to Sparta."
    locations.append(athens_greece)

    sparta_greece = Locations(None, 11, None, None, None, None, None, None)
    sparta_greece.description = "Sparta, once a mighty city, now lay in barrenness. Their constant state of warring caused " \
                                "their economy and population to be run dry.\n" \
                                "Go north east to Athens."
    locations.append(sparta_greece)

    return locations

def health_conditions(health):
    """Function determines health conditions"""
    if health <= 200:
        print("you are in good condition\n")
    elif health <= 125:
        print("You are in mediocre condition\n")
    elif health <= 75:
        print("You are in poor condition. Get some sleep or something to eat or drink.\n")
    else:
        print("You are in horrible condition. Sleep, eating, or drinking is REQUIRED!!!!\n")

def energy_conditions(energy):
    """Function determines energy conditions"""
    if energy <= 50:
        print("Your energy is low, get some sleep\n")

def hunger_thirst_conditions(hunger, thirst):
    """Function determines hunger and thirst conditions"""
    if hunger >= 8:
        print("You are a hungry boy. Get something to eat.\n")
    if thirst >= 8:
        print("You are a thirsty boy. Get something to drink.\n")

def german_list():
    """Creation of Germans"""
    german_list = []
    for i in range(5500):
        german = German.Germans()
        german_list.append(german)
        # Creation of 5500 German opponents
    return german_list

def roman_solider_list():
    """Creation of Roman soldiers"""
    roman_soldiers = []
    for i in range(2500):
        roman = RomanSoldier.Roman_Soldier()
        roman_soldiers.append(roman)
        # Creation of 2500 Roman soldiers
    return roman_soldiers

def roman_civilian_list():
    """Creation of Roman civilians"""
    roman_civ = []
    for i in range(500000):
        rome = RomanCitizen.RomanCitizens()
        roman_civ.append(rome)
        # Creation of 500,000 Roman civilians
        # I know that Rome only had 5,000,000 civilians. I tried to apply five million, but it took to long to load
        # Each turn, per if one German is on Roman/Italian soil, a Roman civilian dies
    return roman_civ

def caesar_rest(caesar, roman_soldiers):
    caesar.health = 100
    caesar.energy = 200
    for i in range(len(roman_soldiers)):
        roman_soldiers[i].health = 50
    print("Congrats. You and your army have rested up")
    return roman_soldiers

def caesar_eat(caesar, supplies_list):
    caesar.hunger = 0
    caesar.energy += random.randrange(1, 10)
    caesar.health += 10
    """binary search through supplies list, for keyword food"""
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
    return supplies_list

def caesar_drink(caesar, supplies_list):
    caesar.thirst = 0
    caesar.energy += random.randrange(1, 5)
    caesar.health += 4
    """binary search through supplies list for water"""
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
    return supplies_list

def stats(caesar, citizens, soldiers, supplies):
    # If function that shows player their stats
    print(f"your energy levels are {caesar.energy}")
    print(f"you have {caesar.health} health pts")
    print(f"you have {caesar.thirst} thirst pts")
    print(f"you have {caesar.hunger} hunger pts")
    print(f"you have {len(soldiers)} soldiers left")
    print(f"There are {len(citizens)} citizens left")
    for food in range(len(supplies)):
        print(f"{food + 1}", supplies[food])

def random_event_soldier(caesar, total_miles_travelled, roman_soldiers):
    if total_miles_travelled % 20 == 5:
        """
        Random event that allows you to gain more soldiers
        """
        legion_additions = random.randrange(1, 1000)
        print(f"Congrats you have stumbled across {legion_additions} people who would like to join the Roman cause")
        caesar_response = input("Will you accept?: ")
        if caesar_response.lower() == "yes" or caesar_response.lower() == "y":
            for add in range(0, (legion_additions + 1)):
                roman_soldiers.append(roman_soldiers[add])
    return roman_soldiers

def main():
    total_miles_travelled = 0
    supplies_list = ["food", "food", "food", "water", "water", "water\n"]
    death = 0
    choices = ["Move",
               "Stop and rest",
               "Eat",
               "Drink",
               "View Map",
               "Quit",
               "View Stats"]
    # Choices that Caesar has

    directions = ["\nNorth",
                  "North East",
                  "North West",
                  "South",
                  "South East",
                  "South West",
                  "East",
                  "West\n"]

    german_warriors = german_list()
    # creation of german list
    roman_soldiers = roman_solider_list()
    # creation of roman soldier list
    roman_citizens = roman_civilian_list()
    # creation of roman civilian list

    caesar = JuliusCaesar()
    current_country = 0
    alive = True
    major_cities = locations()

    print("Welcome player. You will be playing as Julius Caesar. You are currently in the territory of the barbaric"
          " German tribes.\nYou've recently scored a major victory against the Germans, however your legions were "
          "desimiated.\nHowever, you still have 2500 soldiers left. You are to return to Naples Rome, all the while; "
          "gathering more troops and supplies along the way.\nYou will be able to sight see many of the cities Rome has conquered"
          " or will conquer. Be warned though, you may have won a battle against the Germans,\nbut you haven't scared them into "
          "submission. There's still many bands of Germans across Germany and Roman soil.\nTry to avoid contact at all costs and "
          "return to Naples as quickly as possible, since they are after Roman wealth as well.\n:")

    while alive is not False:
        print(major_cities[current_country].description)
        for i in range(len(choices)):
            print((i + 1), choices[i])
        try:
            caesar_choice = int(input("\nWhat would you like to do?: "))

            if caesar_choice == 1 or caesar_choice == 1:
                """Through moving, Caesar loses energy and gains hunger and thirst.
                Since there are Germans everywhere, even in Rome's territory
                , Caesar is also most likely going to run into some.
                """
                troop_exhaustion = 0
                caesar.energy -= random.randrange(1, 50)
                caesar.health -= random.randrange(1, 60)
                caesar.hunger += random.randrange(1, 5)
                caesar.thirst += random.randrange(1, 5)
                for march in range(len(roman_soldiers)):
                    roman_soldiers[march].health -= random.randrange(0, 5)
                    if roman_soldiers[march].health <= 25:
                        troop_exhaustion += 1
                        print("your troops are tired. Let them rest")
                    elif roman_soldiers[march].health <= 0:
                        roman_soldiers.remove(roman_soldiers[march])

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
                roman_soldiers = caesar_rest(caesar, roman_soldiers)

            elif caesar_choice == 3 or caesar_choice == 3:
                supplies_list = caesar_eat(caesar, supplies_list)

            elif caesar_choice == 4 or caesar_choice == 4:
                # If statement if user chooses to eat
                supplies_list = caesar_drink(caesar, supplies_list)

            # elif caesar_choice.lower() == "view map" or caesar_choice.lower() == "v":
            # If statement that shows user where they are

            elif caesar_choice == 6 or caesar_choice == 6:
                # If function that closes game if user chooses to
                print("good choice\n"
                      "goodbye")
                break

            elif caesar_choice == 7 or caesar_choice == 7:
                stats(caesar, roman_citizens, roman_soldiers, supplies_list)

            else:
                print("I'm sorry that option is not available. Just remember there are Germans everywhere, who are after"
                      " you and your people.\nYou better hurry up.")
        except:
            print("You are supposed to insert the specific number to your choice.\n")

        roman_soldiers = random_event_soldier(caesar, total_miles_travelled, roman_soldiers)
        # Function, that adds more soldiers to your armada

        if total_miles_travelled % 12 == 8:
            """Creation of random event.
                Caesar runs into group of Germans and loses heatlh, energy, and troops, due to fighting with 
                group. Group of Germans also take some blows.
                I can't make this a separate module, since i need to return more than one value
            """
            germans = random.randrange(len(german_warriors) // 10)
            print(f"You encountered a group of angry germans with {germans} members")
            caesar.health -= random.randrange(germans)
            caesar.energy -= random.randrange(germans // 2)
            losses = 0
            german_losses = 0
            for ambush in range(germans):
                roman_soldiers[ambush].health -= random.randrange(germans)
                if roman_soldiers[ambush].health <= 0:
                    losses += 1
                    caesar.troop_loss += 1
                    roman_soldiers.remove(roman_soldiers[ambush])
                if german_warriors[ambush].health <= 0:
                    german_losses += 1
                    caesar.score_card += 1
                    german_warriors.remove(german_warriors[ambush])
            print(f"You lost {200 - caesar.health} health pts")
            print(f"You lost {100 - caesar.energy} energy pts")
            print(f"You lost {losses} troops")
            print(f"However you did defeat {german_losses} germans")

        for i in range(len(german_warriors)):
            german_warriors[i].location = random.randrange(len(major_cities))
            if german_warriors[i].location == 5 or german_warriors[i].location == 6 or german_warriors[i].location == 7 \
                    or german_warriors[i].location == 8:
                death += 1
                caesar.civilian_loss += 1
        """Since the germans are moving around regardless of what Caesar is doing...if a specific german warrior's
            location is centered around the indices of any Roman city, then one Roman civilian dies per turn.
        """
        for loss in range(0, (death + 1)):
            roman_citizens.remove(roman_citizens[loss])
        death = 0

        if caesar.health <= 0 or caesar.energy <= 0 or (caesar.hunger >= 15 and caesar.thirst >= 15):
            print("You have died")
            break

        energy_conditions(caesar.energy)
        health_conditions(caesar.health)
        hunger_thirst_conditions(caesar.hunger, caesar.thirst)

        if len(roman_soldiers) <= 0:
            print("Your armada of soldiers no longer exists and you are surrounded")
            break

        if len(german_warriors) <= 0:
            print("Congrats you defeated every German")
            break

main()
"""country = []
for countries in range(len(LocationDescriptions.locations())):
    country.append(LocationDescriptions.locations()[countries].description)

print(country[1])"""