#global variable

game_still_going = True
winner = None
current_player = "X"

# Score of players
score_x = 0
score_o = 0

#board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#display board
def display_board():
  print(" "+board[0]+" | "+board[1]+" | "+board[2])
  print("----"+"---"+"----")
  print(" "+board[3]+" | "+board[4]+" | "+board[5])
  print("----"+"---"+"----")
  print(" "+board[6]+" | "+board[7]+" | "+board[8])

#handle turn
def handle_turn(current_player):
  valid = False
  while not valid:
    print("Player "+ str(current_player)+ " Turn")
    position = input("Choose a position from 1 to 9 : ")
  
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Please choose between 1 to 9")
      
    position = int(position)-1

    if board[position] == "-":
      valid = True
    else:
      print("That position is already filled")
  
  board[position] = current_player
  display_board()
  
#play game
def play_game():
  global score_x, score_o
  # display initial board
  display_board()
  # handling turn
  while game_still_going:
    # handle single turn of a player
    handle_turn(current_player)

  #check if game is over 
    check_if_game_over()

  #flip player
    flip_player()

  #game has ended
  if winner == "X":
    score_x += 1
    print(winner + " won.")
  elif winner == "O":
    score_o += 1
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


def  check_if_game_over():
  check_for_winner()

  check_if_tie()

 #check Win
def check_for_winner():
  global winner
  #check rows
  row_winner = check_row_winner()
  #check columns 
  column_winner = check_column_winner()
  #check diagonals
  diagonal_winner = check_diagonal_winner()

  if row_winner == "X" or row_winner == "O":
    winner = row_winner
  elif column_winner == "X" or column_winner == "O":
    winner = column_winner
  elif diagonal_winner == "X" or diagonal_winner == "O":
    winner = diagonal_winner
  else:
    winner = None
      
  return

#checking for row winner  
def check_row_winner():
  global game_still_going

  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"

  if row1 or row2 or row3:
    game_still_going = False

  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  return
#check for column winner
def check_column_winner():
  global game_still_going

  col1 = board[0] == board[3] == board[6] != "-"
  col2 = board[1] == board[4] == board[7] != "-"
  col3 = board[2] == board[5] == board[8] != "-"

  if col1 or col2 or col3:
    game_still_going = False

  if col1:
    return board[0]
  elif col2:
    return board[1]
  elif col3:
    return board[2]
  return
# check for diagonal winner
def check_diagonal_winner():
  global game_still_going

  dia1 = board[0] == board[4] == board[8] != "-"
  dia2 = board[2] == board[4] == board[6] != "-"

  if dia1 or dia2:
    game_still_going = False

  if dia1:
    return board[4]
  elif dia2:
    return board[4]
  
  return
    
#check tie
def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return
  
#flip player
def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"

  elif current_player == "O":
    current_player = "X"
  return

#Main 
# Play again
while True:
  play_game()
  
  # Print score after game end
  print("Player O gained " + str(score_o) + " points")
  print("Player X gained " + str(score_x) + " points")
  
  # TODO: Add support for "no", "N" and so on
  if input("Play again (y/n): ") == "n":
    break;

  # Reset gameboard
  board = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]
 
  # Variables too
  game_still_going = True
  current_player = winner
  winner = None
  

  # Reset scores
  # TODO: Add support for "yes", "Y"
  if input("Reset score (y/n): ") == "y":
    score_x = 0
    score_y = 0



  




