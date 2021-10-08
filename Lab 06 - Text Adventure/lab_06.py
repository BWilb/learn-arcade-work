class Room():
    def __init__(self, descript, north, east, south, west):
        """
        this function takes in the parameters of an object created from class
        """
        self.description = descript
        self.north = north
        self.south = south
        self.west = west
        self.east = east

def main():
    """
    This function is the main function
    """
    done = False
    current_room = 0
    room_list = []
    room = Room("You are standing in your bed room. There is a mahogany bed to your south. \n"
                "In order to access the rest of the house, step through the marble doorway in front"
                " of you."
                , 1, None, None, None)
    room_list.append(room)
    """this is the first room"""

    room = Room("You are now standing in the center of the house. To your west is the west wing. \n"
                "To your east is the east wing. To your north is the north hall.\n"
                "Behind you is the bedroom.", 5, 4, 0, 2)
    room_list.append(room)
    """this is the second room"""

    room = Room("You are now standing in the west hall of the house. In front of you is the cellar of the house.\n"
                "You can actively hear two drunk people fighting, so it would best be advised not to go there.\n"
                "Behind you is center of the house.", None, 1, None, 3)
    room_list.append(room)
    """this is the third room"""

    room = Room("You are standing in the cellar. It is cold and damp; also the two drunks fighting each other "
                "knocked themselves unconscious, so they aren't dangerous to you.\n"
                "Go east to reenter the west hall.", None, 2, None, None)
    room_list.append(room)
    """this is the fourth room"""

    room = Room("You are standing in the east hall of the house. In front of you is the kitchen of the house.\n"
                "Behind you is the center of the house", None, 5, None, 1)
    room_list.append(room)
    """this is the fifth room"""

    room = Room("You are now standing in the kitchen. Your maid is making broasted chicken and stuffed turkey for"
                " dinner.\n Behind is the east hall.", None, None, None, 4)
    room_list.append(room)
    """this is the sixth room"""

    room = Room("You are standing in the north hall. The walls are a glorious lavender with pictures of " 
                "suns on them.\n To your north is the lounge room and to your south is the center of the house.",
                7, None, 1, None)
    room_list.append(room)
    """this is the seventh room"""

    room = Room("You are now standing in the lounge room. There is a TV set to the Bloomberg channel.\n" 
                "To the north is a balcony and to your south is the north hall.", 8, None, 5, None)
    room_list.append(room)
    """this is the eigth room"""

    room = Room("You are standing out on a terraced balcony. To your south is the lounge room.\n"
                "The view outside the house is amazing. Just don't get to close!", None, None, 6, None)
    room_list.append(room)
    """this is the ninth room"""

    while not done:
        """
        beginning of the while statement
        """
        print()
        print(room_list[current_room].description)
        user_choice = input("which direction would you like to go? if you would like to quit, enter quit ")

        if user_choice.lower() == "north" or user_choice.lower() == "n":
            next_room = room_list[current_room].north
            if room_list[current_room].north is None:
                print("You can't go north!!")
            else:
                current_room = next_room

        elif user_choice.lower() == "south" or user_choice.lower() == "s":
            next_room = room_list[current_room].south
            if room_list[current_room].south is None:
                print("you cant go that way")
            else:
                current_room = next_room

        elif user_choice.lower() == "east" or user_choice.lower() == "e":
            next_room = room_list[current_room].east
            if room_list[current_room].east is None:
                print("you cant go that way")
            else:
                current_room = next_room

        elif user_choice.lower() == "west" or user_choice.lower() == "w":
            next_room = room_list[current_room].west
            if room_list[current_room].west is None:
                print("you cant go that way")
            else:
                current_room = next_room

        elif user_choice.lower() == "quit" or user_choice.lower() == "q":
            print("you chose to quit. please play again")
            done = False
            break
        else:
            print("I dont understand what you mean")

main()
