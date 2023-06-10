# My version of Tic-Tac-Toe with two people!


print(
    "Welcome to Tic-Tac-Toe. The board is numbered 0-8; 0 being the top left corner and 8 being the bottom right. Have fun!"
)

# Starts off with empty board (dashes are to help seperate
board = ["-"] * 9


# Main function which prints the board into a readable state
def printBoard():
    print(f"{(board[0])}|{(board[1])}|{(board[2])}")
    print("-----")
    print(f"{(board[3])}|{(board[4])}|{(board[5])}")
    print("-----")
    print(f"{(board[6])}|{(board[7])}|{(board[8])}")


# Main game loop
while True:
    # This section makes sure the player only inputs integers (0-8) and the 
    # position they want to play can't overwrite another player's moves
    while True:
        try:
            player1Position = int(input("P1, Please select a place to play: "))
            if player1Position < 0 or player1Position > 8:
                raise ValueError
            elif board[player1Position] != "-":
                raise ValueError
            break
        except ValueError:
            print("Oops! Not a valid spot or number. Try again.")

    player1Choice = "X"
    # deletes '-' character and insert's PLayer 1's 'X'
    del board[player1Position]
    board.insert((player1Position), (player1Choice))
    printBoard()

    # Win conditions for PLayer 1 (I'm sure there is a better way to do this)
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("Player 1 wins!")
        break
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("Player 1 wins!")
        break
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("Player 1 wins!")
        break
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("Player 1 wins!")
        break
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("Player 1 wins!")
        break
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("Player 1 wins!")
        break
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        print("Player 1 wins!")
        break
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("Player 1 wins!")
        break

    if "-" not in board:
        print("Cat's game!")
        break

    # Same as Player 1's block to catch faulty inputs and prevent cell overwrites
    while True:
        try:
            player2Position = int(input("P2, Please select a place to play: "))
            if player2Position < 0 or player2Position > 8:
                raise ValueError
            elif board[player2Position] != "-":
                raise ValueError
            break
        except ValueError:
            print("Oops! Not a valid spot or number. Try again.")

    player2Choice = "O"
    # same delete '-' and insert 'O'
    del board[player2Position]
    board.insert((player2Position), (player2Choice))
    printBoard()

    # Player 2 win conditions (could be improved)
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        print("Player 2 wins!")
        break
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        print("Player 2 wins!")
        break
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        print("Player 2 wins!")
        break
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        print("Player 2 wins!")
        break
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        print("Player 2 wins!")
        break
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        print("Player 2 wins!")
        break
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        print("Player 2 wins!")
        break
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        print("Player 2 wins!")
        break

    if "-" not in board:
        print("Cat's game!")
        break
