class Room:
    def __init__(self, description, north, east, south, west):
        self.description = ""
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0


def main():
    room_list = []
    room = Room("You are in the Storage Room of a house.",
                None,
                None,
                3,
                None)
    room_list.append(Room)
    room = Room("You are in a bedroom of a house.",
                None,
                None,
                4,
                None)
    room_list.append(Room)
    room = Room("You are in the Entrance Hall to a house.",
                None,
                None,
                None,
                3)
    room_list.append(Room)
    room = Room("You are in the West Hall of a house.",
                0,
                2,
                6,
                4)
    room_list.append(Room)
    room = Room("You are in the East Hall of a house.",
                1,
                3,
                7,
                5)
    room_list.append(Room)
    room = Room("You are in a bedroom in a house.",
                None,
                4,
                None,
                None)
    room_list.append(Room)
    room = Room("You are in the dining room of a house.",
                3,
                None,
                None,
                7)
    room_list.append(Room)
    room = Room("You are in the kitchen of a house.",
                4,
                None,
                None,
                6)
    room_list.append(Room)
    current_room = 0
    print(room_list, current_room)


main()