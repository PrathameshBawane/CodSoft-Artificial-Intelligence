import math

# Initialize the board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for winner
def winner(board, player):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # cols
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_states)

# Check for draw
def is_draw(board):
    return ' ' not in board

# Get empty cells
def get_empty_cells(board):
    return [i for i in range(9) if board[i] == ' ']

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if winner(board, 'O'):
        return 1
    if winner(board, 'X'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in get_empty_cells(board):
            board[i] = 'O'
            score = minimax(board, depth + 1, False)
            board[i] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in get_empty_cells(board):
            board[i] = 'X'
            score = minimax(board, depth + 1, True)
            board[i] = ' '
            best_score = min(best_score, score)
        return best_score

# Best move for AI
def best_move():
    best_score = -math.inf
    move = None
    for i in get_empty_cells(board):
        board[i] = 'O'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    board[move] = 'O'

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X. AI is O.\n")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'X'
        print_board()

        if winner(board, 'X'):
            print("You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # AI move
        best_move()
        print("AI move:")
        print_board()

        if winner(board, 'O'):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

# Run the game
play_game()
