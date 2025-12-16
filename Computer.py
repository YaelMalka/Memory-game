from Player import Player
from random import randint

class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_card(self,size):
        place=randint(0,size-1)
        return place