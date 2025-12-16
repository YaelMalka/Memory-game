from Card import Card
from Enum import EnumCardStatus
from Player import Player
from random import randint
import math

class BoardGame():
    def __init__(self,size=16):
        self.size=size        
        self.arrayCard=[Card() for i in range(size)]
    
    def init_board(self):  
       for i in range(self.size//2):     
          flag=True
          while flag==True:
            flag=False             
            num=randint(1, (self.size//2))        
            for card in self.arrayCard:
              if card.content==num:
                flag=True
          
          for j in range(2):
            check=True
            while check==True:
              check=False
              place=randint(0, self.size-1)
              if self.arrayCard[place].content!=0:
                  check=True
            self.arrayCard[place].content=num 
                 
    
    def print_board(self) : 
       cnt=0
       for i in self.arrayCard:
            if i.status== EnumCardStatus.DISCOVER:
               print(i.content,end=" , ")
            elif  i.status== EnumCardStatus.COVER:
               print('__',end=" , ")
            else:
               print("👍",end=" , ")
            cnt+=1
            if (cnt)%int(math.sqrt(self.size))==0 :
                  print()

    def check_legal_card(self,place,type):
        if type=="Player":
          while place<0 or place>=self.size or self.arrayCard[place].status!=EnumCardStatus.COVER:
             place=int(input("the place is not legal try choose anothr place"))
        else:
             while place<0 or place>=self.size or self.arrayCard[place].status!=EnumCardStatus.COVER:
                 place=randint(0,self.size-1)
        return place 
    
    def cards_cover(self):
      for card in self.arrayCard:
          if card.status == EnumCardStatus.COVER:
              return True
      return False
    
    def find_couple(self,place1,place2):
              self.arrayCard[place1].status=EnumCardStatus.TAKEN
              self.arrayCard[place2].status=EnumCardStatus.TAKEN

# מציג לי את המערך לאחר רינדום מספרים לתוכו לשם הנוחות שלי בלבד
    def print(self):
        cnt=0
        for i in self.arrayCard:
            print(i.content,end=" , ")
            cnt+=1
            if (cnt)%int(math.sqrt(self.size))==0 :
                  print()
        
          
                  
               
               
       
    

