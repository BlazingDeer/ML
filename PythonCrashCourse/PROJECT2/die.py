from random import randint

class Die:
    """Klasa reprezentująca pojedyńczą kostkę do gry."""

    def __init__(self,num_sides=6):
        """Przyjmij kostke z 6 stronami"""
        self.num_sides=num_sides

    def roll(self):
        """retur a random valuie between 1 and number of sides"""
        return randint(1,self.num_sides)