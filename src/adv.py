from room import Room
import random
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# Dicitionary for items

items = [
    Item('Syringe', 'More Health'),
    Item('Coins', 'Cash on Hand'),
    Item('Sword', 'Sharp - keep away from eyes.'),
    Item('Gun', 'Protect yourself if the swords break'),
    Item('Rocket Launcher', 'Just In Case')
]

items_len = len(items)

room['foyer'].items.append(items[random.randrange(items_len)])
room['outside'].items.append(items[random.randrange(items_len)])
room['overlook'].items.append(items[random.randrange(items_len)])
room['narrow'].items.append(items[random.randrange(items_len)])
room['treasure'].items.append(items[random.randrange(items_len)])
# Making a function to iterate the above

def get_idx(lst, value):
    for i, dic in enumerate(lst):
        print(f'{i} -- {dic} /// {value}')
        if dic.name == value:
            return i
    return -1


# tuple for directions 
# tuples don't change
directions = ('n', 'e', 's', 'w')
# tuple for options a player can select 
# tuple doesnt change
actions = ('z', 'd', 'x', 'v')

player_name = input("Welcome to the best Adventure, enter your name to continue")
player_one = Player(player_name, room['outside'])

print(f'Welcome, {player_one.name}, you are in {player_one.current_room}.')


while True:
    cmd = input("""Select a direction [n,e,s,w] for your character to travel. Inspect room for items using [inspect] 
        
        ~~~>""")

    print(f'cmd --> {cmd}')
   

    if cmd == 'inspect':
        print(player_one.current_room.list_items())

    elif cmd == 'i' or cmd == 'inventory':
        player_one.print_inventory()

    elif 'get' in cmd:
        item_str = cmd.split(' ', )[1]
        print(f'{player_one.name} is attempting to get {item_str}')

        item_idx = get_idx(player_one.current_room.items, item_str)

        if item_idx >= 0:
            player_one.inventory.append(
                player_one.current_room.items[item_idx])
            player_one.current_room.items.pop(item_idx)
        else:
            print(f'{item_str} is not in {player_one.current_room}')

    elif 'drop' in cmd:
        pass
        item_str = cmd.split(' ',)[1]
        print(
            f'You are dropping {item_str} inside of {player_one.current_room}')
        item_idx = get_idx(player_one.inventory, item_str)

        if item_idx >= 0:
            player_one.inventory.pop(item_idx)
            player_one.current_room.items.append(
                player_one.inventory[item_idx])

    elif cmd in directions:
        player_one.move(cmd)

    elif cmd == 'q':
        print("Quitting Adventure, you'll coward")
        break

else: 
    print('Please provide a valid cardinal direction [n, e, s, w] or enter q to quit.')
