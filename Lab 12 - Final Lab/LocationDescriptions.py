
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
                                 "legions get out before you yourself are killed. Go south to Munich"
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
                                 "we first defeated the Germanic barbarians. \n Now the city lies smoldering. Go east to" \
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