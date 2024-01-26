# Tic Tac Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check for a win
def check_win(player):
    # Check rows
    if (board[0] == board[1] == board[2] == player) or \
       (board[3] == board[4] == board[5] == player) or \
       (board[6] == board[7] == board[8] == player):
        return True
    # Check columns
    if (board[0] == board[3] == board[6] == player) or \
       (board[1] == board[4] == board[7] == player) or \
       (board[2] == board[5] == board[8] == player):
        return True
    # Check diagonals
    if (board[0] == board[4] == board[8] == player) or \
       (board[2] == board[4] == board[6] == player):
        return True
    return False

# Function to play the game
def play_game():
    print("Let's play Tic Tac Toe!")
    print_board()
    player = 'X'
    while True:
        position = int(input("Enter a position (1-9): "))
        if board[position - 1] == ' ':
            board[position - 1] = player
            print_board()
            if check_win(player):
                print(player, "wins!")
                break
            if ' ' not in board:
                print("It's a tie!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid position. Try again.")

# Start the game
play_game()