# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    """Information for current player in game."""
    inventory = []

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'{self.name}, {self.current_room}'

    def __repr__(self):
        return f'{self.name}, {self.current_room}'

    def print_current_room(self):
        print(f'{self.name} is currently in {self.current_room}')

    def move(self, direction):
        # check if user can move in that direction
        if getattr(self.current_room, f'{direction}_to'):
            print(f'{self.name} fumbles from {self.current_room}...')
            self.current_room = getattr(self.current_room, f'{direction}_to')
            print(f'''...to...
            {self.current_room}, {self.current_room.description}
            ''')
        else:
            print('Player cannot move that direction from here.')

    def print_inventory(self):
        if len(self.inventory) > 0:
            print(f'You are carrying {self.inventory}')

        else:
            print('Your inventory is empty.')