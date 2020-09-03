# Items that exist in a room and/or players inventory

class Item:
    """ 
    Class that represents items in 
    a players room and/or inventory
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.description}'
    def __repr__(self):
        return f'{self.name} ----{self.description}'
    
    def pick_up(self):
        print(f'You picked up {self.name}')
    
    def drop(self):
        print(f'You have dropped an item {self.name}')