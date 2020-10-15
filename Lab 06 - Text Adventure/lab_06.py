class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    room = Room("You are in the storage room.\nThere is a door to the south that leads to part of the living room.",
                None,
                None,
                3,
                None)
    room_list.append(room)
    room = Room("You are in the north bedroom.\nThere is a door to the south that leads to part of the living room.",
                None,
                None,
                4,
                None)
    room_list.append(room)
    room = Room("You are in the entryway to a house.\nIt leads to the east.",
                None,
                3,
                None,
                None)
    room_list.append(room)
    room = Room("You are in the west part of the living room.\nThere are doors to the north, west, south, and to the "
                "east\nis another part of the living room.",
                0,
                4,
                6,
                2)
    room_list.append(room)
    room = Room("You are in the east part of the living room.\nThere are doors to the north, east, south, and to the "
                "west\nis the other part of the living room.",
                1,
                5,
                7,
                3)
    room_list.append(room)
    room = Room("You are in the east bedroom.\nThere is a door to the west that leads to part of the living room.",
                None,
                None,
                None,
                4)
    room_list.append(room)
    room = Room("You are in the dining room.\nThere are doors to the north and east.",
                3,
                7,
                None,
                None)
    room_list.append(room)
    room = Room("You are in the kitchen.\nThere are doors that lead to the north and to the west.",
                4,
                None,
                None,
                6)
    room_list.append(room)
    current_room = 2

    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("Where do you want to go? ")

        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "q" or user_input.lower() == "quit":
            done = True

        else:
            print()
            print("Input not understood.")


main()
