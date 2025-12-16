from Enum import EnumCardStatus
class Card:
    def __init__(self):
        self.content=0
        self.status=EnumCardStatus.COVER

    def equal(self,card):
      return card.content==self.content  
    
    def __str__(self):
       return f"content:{self.content} status:{self.status} "  
    
    def change_status(self,status):
       self.status=status
       