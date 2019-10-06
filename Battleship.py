'''
Program:    Python Battleship
Dev:        Jackson Carlton
Date:       01/14/2019
'''
from random import randint

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def main():
    board = [] #Set up board
    print("Welcome to Python Battleship!")
    print("Here is the empty Battleship Gameboard: ")
    for x in range(0, 6):
      board.append(["O"] * 6)
    print_board(board) #prints 6 x 6 board to the screen
    ship_row = random_row(board) #Location of ship
    ship_col = random_col(board)

    print("You'll have 4 attempts to hit the battleship.") #Game
    for turn in range(4):
      print("Turn", turn + 1)
      guess_row = int(input("Guess Row: "))
      guess_col = int(input("Guess Col: "))
      if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
      else:
        if guess_row not in range(5) or \
          guess_col not in range(5):
          print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
          print("You guessed that one already.")
        else:
          print("You missed my battleship!")
          board[guess_row][guess_col] = "X"
        print_board(board)
        if turn == 3:
          print("Game Over")

main()
