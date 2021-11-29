locations = []
object_list = []
user_name = "Hello user, you are playing as Julius Caesar. Try not to die!!"

class Location():
    def __int__(self, north, east, south, west):
        self.description = None
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def cities():
    done = False
    current_room = 0
    rome_italy = Location(None, None, 1, None)
    rome_italy.description = (user_name + " You are currently stationed in Rome Italy. Explore around your empire.")
    locations.append(rome_italy)
    naples_italy = Location(0, None, None, None)
    naples_italy.description = ("Julius; you've moved down south to Naples. ")
