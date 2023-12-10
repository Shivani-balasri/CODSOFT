import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'Tie': 0}

    if is_winner(board, 'X'):
        return -1

    if is_winner(board, 'O'):
        return 1

    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            new_board = copy.deepcopy(board)
            new_board[move[0]][move[1]] = 'O'
            eval = minimax(new_board, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            new_board = copy.deepcopy(board)
            new_board[move[0]][move[1]] = 'X'
            eval = minimax(new_board, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for move in get_available_moves(board):
        new_board = copy.deepcopy(board)
        new_board[move[0]][move[1]] = 'O'
        move_val = minimax(new_board, 0, False)

        if move_val > best_val:
            best_move = move
            best_val = move_val

    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            try:
                row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
                if board[row][col] != ' ':
                    print("Invalid move! Cell already taken. Try again.")
                    continue
            except ValueError or IndexError:
                print("Invalid input! Please enter two integers separated by space.")
                continue
        else:
            row, col = get_best_move(board)

        board[row][col] = current_player

        if is_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
