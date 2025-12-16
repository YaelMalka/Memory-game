
from Board import BoardGame
from Computer import Computer
from Enum import EnumCardStatus
from Player import Player


class Game():    
    def __init__(self,size=16):
       self.board=BoardGame(size)
       self.playerList=[Player("yael"),Computer("computer")]
       self.index=0 


    def init_board(self):
        self.board.init_board()

    def print_board(self):
        self.board.print_board()

    def print(self):
       self.board.print()
        
    def find_couple(self):
      for i in range(self.board.size):
         for j in range(self.board.size):
            if self.board.arrayCard[i].content==self.board.arrayCard[j].content and self.board.arrayCard[i].status==self.board.arrayCard[j].status and self.board.arrayCard[j].status==EnumCardStatus.DISCOVER and i!=j:
               self.playerList[self.index].listCard.append(self.board.arrayCard[i])
               self.playerList[self.index].listCard.append(self.board.arrayCard[j])
               self.playerList[self.index].score+=1
               self.board.find_couple(i,j)
               return True
      return False

    def winner(self):
      max=0
      imax=0
      for i in range(len(self.playerList)):        
          if self.playerList[i].score>max:
             max=self.playerList[i].score
             imax=i
      print(f"{self.playerList[imax].name} is the winner!")
      print("the score in the game= ",max)
      print("the cards I earned= ",end=" ")
      self.playerList[imax].present_all_cards()
       
    def real_game(self):
       while self.board.cards_cover():
          self.index=self.index%len(self.playerList)
          play=self.playerList[self.index]
          print(self.playerList[self.index].name)
          for j in range(2):
            placeCard=int(play.choose_card(self.board.size))
            if type(self.playerList[self.index])  is Player:
               placeCard =self.board.check_legal_card(placeCard,"Player")
            else:
               placeCard =self.board.check_legal_card(placeCard,"Computer")               
            self.board.arrayCard[placeCard].change_status(EnumCardStatus.DISCOVER)
          self.board.print_board()
          if self.find_couple()==False:
             for k in self.board.arrayCard:
                if k.status==EnumCardStatus.DISCOVER:
                    k.change_status(EnumCardStatus.COVER)
                        
          self.index+=1
       self.winner() 
       
                   
                   

          
            
       
       
       
        
    