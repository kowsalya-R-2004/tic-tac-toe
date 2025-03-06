# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to play Tic-Tac-Toe
def play_game():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Display initial empty board
    print_board(board)
    
    current_player = "X"
    
    # Loop until the game is over
    while True:
        print(f"Player {current_player}'s turn")
        
        # Get player input for row and column
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        
        # Check if the cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already taken, try again.")
            continue
        
        # Display updated board
        print_board(board)
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (tie game)
        if is_board_full(board):
            print("It's a tie!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()
