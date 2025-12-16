from Card import Card

class Player:
    def __init__(self,name) :
        self.name=name
        self.score=0
        self.listCard=[]
    
    def choose_card(self,size):
        place=(int)(input(f"enter card place you want to open from 0 to {size}: "))
        return place
    
    def present_all_cards(self):
        for item in self.listCard:
            print(item.content,end=' ,')
        print()


    


