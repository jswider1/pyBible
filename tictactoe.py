# tuples are unchangeable
# board needs to have 9 elements
# loop inside statement to create nine spaces
board = [" " for i in range(9)]
print(board) # without formatting

# this is our board formatted
def print_board():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == "X":
        player = 1
    elif icon == "O":
        player = 2
    
    print("Your turn player {}.".format(player))
    choice=int(input("Enter your move, choose a position (1-9): ").strip())
    if board[choice-1]==" ":
        if player == 1:
            board[choice-1]="X"
        else:
            board[choice-1]="O"
    else:
        print()
        print("That space is taken, select another. ")
        player_move(icon)


def is_victory(icon):
    if(board[0]==board[1]==board[2]==icon) or \
      (board[3]==board[4]==board[5]==icon) or \
      (board[6]==board[7]==board[8]==icon) or \
      (board[0]==board[3]==board[6]==icon) or \
      (board[1]==board[4]==board[7]==icon) or \
      (board[2]==board[5]==board[8]==icon) or \
      (board[0]==board[4]==board[8]==icon) or \
      (board[2]==board[4]==board[6]==icon):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False
            
while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins!")
        break
    if is_draw():
        print("It's a draw.")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O wins!")
        break
    if is_draw():
        print("It's a draw.")
        break
