
from Game import Game
from Player import Player


def main():
  start=Game("yael",6)#חובה להכניס שם שחקן ואפשרי להגדיר גודל לוח משחק
  start.init_board()
  start.print_board()
  start.real_game()

if __name__ == "__main__":
    main()
