#!/usr/bin/python -tt

# tic-tac-toe in Python
# for Flatiron School
# by Sun Kim


# helper functions:

# checks to see that user has given proper int value
def ask_input(plyr):
  # ask for an int between 0 and 10, non-inclusive
  while (True):
    try:
      inpt = int(raw_input("Your turn, " + plyr + ": \n"))
      # ask for proper input if given input is not between 0 and 10, or already used 
      if inpt < 1 or inpt > 9 or check_board(inpt) == False:
        print "Please give proper integer input (1-9)."
      else:
        break
    # see that user input is a proper integer type
    except ValueError: 
      print "Please give proper integer input (1-9)." 
  return inpt

# check to see user input has not already been given
def check_board(num):
  # if board position is empty, return true, else false
  if ('_' == search_for_position(num) or '_' == search_for_position(num)):
    return True
  else:
    print "That position has already been filled."
    return False

# return the corresponding board position, given user input.
# this can probably be somehow written into one function with set_board() function below...
# ... but I'm not quite sure what would be the best way. 
def search_for_position(num):
  # determine row position for given input
  if num < 4:
    row = 0
  if num >= 4 and num < 7:
    row = 1
  if num >= 7 and num < 10:
    row = 2
  # determine col position for given input
  if not (num % 3) == 0:
    col = (num % 3) - 1
  else:
    col = 2
  # return corresponding board position
  return BOARD[row][col]

# draws 'X' or 'O' on board given player input
def set_board(mark, num):
  # determine row position for given input
  if num < 4:
    row = 0
  if num >= 4 and num < 7:
    row = 1
  if num >= 7 and num < 10:
    row = 2
  # determine col position for given input
  if not (num % 3) == 0:
    col = (num % 3) - 1
  else:
    col = 2
  # mark 'X' or 'O' on board
  BOARD[row][col] = mark

# draws an updated board
def draw_board(board):
  print board[0][0] + " | " + board[0][1] + " | " + board[0][2]
  print board[1][0] + " | " + board[1][1] + " | " + board[1][2]
  print board[2][0] + " | " + board[2][1] + " | " + board[2][2]

# checks if win conditions are met
def is_winner(board):
  # checks to see if any row or columns have winning board arrangement
  for i in range(0,3):
    if board[i][0] == board[i][1] == board[i][2] != "_" or board[0][i] == board[1][i] == board[2][i] != "_":
      return True
  # checks if diagonals have winning board arrangement
  if board[0][0] == board[1][1] == board[2][2] != "_" or board[0][2] == board[1][1] == board[2][0] != "_":
    return True


# main function
def main():
  # declare a global variable called board, so that all functions have access
  global BOARD
  # initialize 3X3 board using list comprehension, which will act like a nested for-loop 
  BOARD = [["_" for i in range(3)] for j in range(3)]

  # instantiate count that will be used later to see if board is full
  count = 0

  # greetings, player!
  print "Are you ready to play Tic-Tac-Toe??"
  print "You will need two players for this game."

  # take in user names
  p1 = raw_input("Please enter your name, player 1: ")
  p2 = raw_input("Ok, your name, player 2: ")
  print ""
  print p1 + ", you will be 'X', and " + p2 + ", you will be 'O'."

  # how to play
  print "Press the corresponding number keys to make your mark on the board:"
  print "1 | 2 | 3"
  print "4 | 5 | 6"
  print "7 | 8 | 9"
  print p1 + " will go first. Let's start!!!"

  # set initial player turn to player 1
  turn = p1
  
  # ask for player input until board is full 
  while (count < 9):
    # player 1's turn
    if turn == p1:
      num = ask_input(p1)
      set_board('X', num)
      draw_board(BOARD)
      # increment count for while condition
      count += 1
      # if there is a winning board arrangement, exit out of loop
      if is_winner(BOARD) == True:
        print p1 + " WINS!!!! Thanks for playing!"
        break
      # change to player 2's turn
      turn = p2

    # player 2's turn
    elif turn == p2:
      num = ask_input(p2)
      set_board('O', num)
      draw_board(BOARD)
      # increment count for while condition
      count += 1
      # if there is a winning board arrangement, exit out of loop
      if is_winner(BOARD) == True:
        print p2 + " WINS!!!! Thanks for playing!"
        break
      # change to player 1's turn
      turn = p1

  # tie game if board is full without winning arrangements
  if is_winner(BOARD) != True:
    print "Tie game. Both of you try harder!!"

if __name__ == '__main__':
  main()