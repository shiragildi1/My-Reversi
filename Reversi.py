#Shira Giladi
import random

#define valu
empty = 0
red = 1
black = 2

#size of board
size_of_board = 8

#The beginning board
def beginning_board():
    return [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

#2 players
players = {
    'RED': 1,
    'BLACK': 2
}

#print board
def print_board(board):
    for row in board:
        print(' '.join(['-', 'R', 'B'][cell] for cell in row))

#check if index exsist in limit of board
def is_on_board(row, col):
    return 0 <= row < size_of_board and 0 <= col < size_of_board

#check if section is valid
def is_valid_move(board, row, col, player):
    if board[row][col] != empty:  # בדיקה אם התא ריק
        return False
    else:
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:  # כל הכיוונים האפשריים
            if check_direction(board, row, col, d_row, d_col, player):
                return True
        return False

#checking for any direction' if valid
def check_direction(board, row, col, d_row, d_col, player):
    row += d_row
    col += d_col
    if is_on_board(row, col) and board[row][col] == 3 - player:
        while is_on_board(row, col) and board[row][col] == 3 - player:
            row += d_row
            col += d_col
        if is_on_board(row, col) and board[row][col] == player:
            return True
    return False

#Changing the opponent's discs to the current player's discs in all directions where the move is legal
def change_discs(board, row, col, player):
    for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:  # כל הכיוונים האפשריים
        if check_direction(board, row, col, d_row, d_col, player):
            flip_discs(board, row, col, player, d_row, d_col)

# Flipping the opponent's discs into the current player's discs in the checked direction
def flip_discs(board, row, col, player, d_row, d_col):
    row += d_row
    col += d_col
    while is_on_board(row, col) and board[row][col] == 3 - player:
        board[row][col] = player
        row += d_row
        col += d_col

# This function returns the current result on the board
def result(board):
    count_red = sum(row.count(red) for row in board)
    count_black = sum(row.count(black) for row in board)
    return f"Red: {count_red}, Black: {count_black}"

# Print the board and the current result
def display(board):
    count_red = sum(row.count(red) for row in board)
    count_black = sum(row.count(black) for row in board)
    print_board(board)
    print("Result:", result(board), "total:", count_red + count_black)
    print("\n")

# A function that returns the direction name
def direction_name(d_row, d_col):
    if d_row == -1 and d_col == 0:
        return "UP"
    elif d_row == 1 and d_col == 0:
        return "DOWN"
    elif d_row == 0 and d_col == -1:
        return "LEFT"
    elif d_row == 0 and d_col == 1:
        return "RIGHT"
    elif d_row == -1 and d_col == -1:
        return "UP_LEFT"
    elif d_row == 1 and d_col == 1:
        return "DOWN_RIGHT"
    elif d_row == -1 and d_col == 1:
        return "UP_RIGHT"
    elif d_row == 1 and d_col == -1:
        return "DOWN_LEFT"

# This function selects the next move according to the legality I defined in the readme file
def choose_move(board, player):
    for row in range(size_of_board):
        for col in range(size_of_board):
            if row <= 2 and col <= 2:  # תחום שמאל עליון
                directions = [(-1, -1), (0, -1), (-1, 0)]
                direction_names = ["UP_LEFT", "LEFT", "UP"]
            elif row <= 2 and 3 <= col <= 4:  # תחום עליון
                directions = [(-1, 0)]
                direction_names = ["UP"]
            elif row <= 2 and col >= 5:  # תחום ימין עליון
                directions = [(-1, 1), (0, 1), (-1, 0)]
                direction_names = ["UP_RIGHT", "RIGHT", "UP"]
            elif 3 <= row <= 4 and col >= 5:  # תחום ימני
                directions = [(0, 1)]
                direction_names = ["RIGHT"]
            elif row >= 5 and col >= 5:  # תחום ימין תחתון
                directions = [(1, 1), (0, 1), (1, 0)]
                direction_names = ["DOWN_RIGHT", "RIGHT", "DOWN"]
            elif row >= 5 and 3 <= col <= 4:  # תחום תחתון
                directions = [(1, 0)]
                direction_names = ["DOWN"]
            elif row >= 5 and col <= 2:  # תחום שמאל תחתון
                directions = [(1, -1), (0, -1), (1, 0)]
                direction_names = ["DOWN_LEFT", "LEFT", "DOWN"]
            elif 3 <= row <= 4 and col <= 2:  # תחום שמאלי
                directions = [(0, -1)]
                direction_names = ["LEFT"]
            else:
                continue  # אם לא מתאים לשום תחום, דלג

            for (d_row, d_col), direction_name in zip(directions, direction_names):
                if is_valid_move(board, row, col, player):
                    print(f"Chosen direction {direction_name} for move at ({row}, {col})")
                    return row, col
    return None, None  # אם אין מהלך חוקי

# This function shows the game moves according to the legality.
def print_play(board, player, current_board, random_move=False, evaluation_function=None):
    print("*******************************************************play**********************************************************************")
    if player != 1:
        print("State 0")
        display(board)
    while True:  # נמשיך עד שלא יהיו מהלכים חוקיים יותר
        if random_move:
            row, col = choose_random_move(board, player)
        elif evaluation_function:
            row, col = find_best_move(board, player, evaluation_function)
            print(f"Evaluation score for {'Red' if player == red else 'Black'}: {evaluation_function(board, player)}")
        else:
            row, col = choose_move(board, player)

        if row is not None and col is not None:
            board[row][col] = player  # הנחת הדיסקית
            change_discs(board, row, col, player)
            current_board += 1
            print("State", current_board)
            print(f"Board after move ({row}, {col}, {'R' if player == red else 'B'}):")
            display(board)
            player = 3 - player  # החלפת שחקן
        else:
            print(f"No valid moves for player {'R' if player == red else 'B'}")
            break
    # return board

#Creating an initial state with 8 disks on the board ie after 4 moves
def state_whith_8_disks(num):
    board = beginning_board()
    movesA = [(5, 4, red), (5, 3, black), (5, 2, red), (6, 3, black)]
    print("State 0")
    display(board)
    current_board = 1
    for move in movesA[:num - 4]:
        row, col, player = move
        if is_valid_move(board, row, col, player):
            board[row][col] = player  # הנחת הדיסקית
            change_discs(board, row, col, player)
            print("Stat", current_board)
            print(f"Board after move ({row}, {col}, {'R' if player == red else 'B'}):")
            display(board)
            current_board += 1
        else:
            print(f"Move ({row}, {col}, {'R' if player == red else 'B'}) is not valid")
    return board

# Q1
def print_A(board):
    print("*******************************************************1-A**********************************************************************")
    print_play(board, 1, 4, random_move=False)

def print_B():
    print("*******************************************************1-B**********************************************************************")
    print_play(beginning_board(), 2, 0, random_move=False)

# This function chooses the next move randomly
def choose_random_move(board, player):
    valid_moves = [(row, col) for row in range(size_of_board) for col in range(size_of_board) if is_valid_move(board, row, col, player)]
    if valid_moves:
        move = random.choice(valid_moves)
        print(f"Chosen random move at ({move[0]}, {move[1]})")
        return move
    return None, None

def print_C():
    print("*******************************************************1-C**********************************************************************")
    print_play(beginning_board(), 2, 0, random_move=True)

# Q2
def H1(board, player):
    count_player = sum(row.count(player) for row in board)
    count_opponent = sum(row.count(3 - player) for row in board)
    return count_player - count_opponent

# A function for examining the evaluation functions on the original board and making the best move
def test_evaluation_functionH1():
    print("*******************************************************2-H1**********************************************************************")
    board = beginning_board()
    player = black
    current_board = 0
    print("State ", current_board)
    display(board)
    while True:
        best_move = find_best_move(board, player, H1)
        if best_move:
            row, col = best_move
            board[row][col] = player
            change_discs(board, row, col, player)
            current_board += 1
            print("State ", current_board)
            print(f"Best move for {'Black' if player == black else 'Red'}: ({row}, {col})")
            print(f"Evaluation score for {'Red' if player == red else 'Black'}: {H1(board, player)}")
            print(f"Board after best move for {'Black' if player == black else 'Red'}:")
            display(board)
            player = 3 - player  # החלפת שחקן
        else:
            print(f"No valid moves for player {'R' if player == red else 'B'}")
            break

# A function to find the best move for the player
def find_best_move(board, player, evaluation_function):
    best_move = None
    best_score = -float('inf')

    for row in range(size_of_board):
        for col in range(size_of_board):
            if is_valid_move(board, row, col, player):
                board_copy = [r[:] for r in board]
                board_copy[row][col] = player
                change_discs(board_copy, row, col, player)
                score = evaluation_function(board_copy, player)
                if score > best_score:
                    best_move = (row, col)
                    best_score = score

    return best_move

def H2(board, player):
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    edges = [(0, i) for i in range(1, 7)] + [(7, i) for i in range(1, 7)] + [(i, 0) for i in range(1, 7)] + [(i, 7) for i in range(1, 7)]

    score = 0
    for row in range(size_of_board):
        for col in range(size_of_board):
            if board[row][col] == player:
                if (row, col) in corners:
                    score += 3
                elif (row, col) in edges:
                    score += 2
                else:
                    score += 1
            elif board[row][col] == 3 - player:
                if (row, col) in corners:
                    score -= 3
                elif (row, col) in edges:
                    score -= 2
                else:
                    score -= 1
    return score

# A function for examining the evaluation functions on the original board and making the best move
def test_evaluation_functionH2():
    print("*******************************************************2-H2**********************************************************************")
    board = beginning_board()
    player = black
    current_board = 0
    print("State ", current_board)
    display(board)
    while True:
        best_move = find_best_move(board, player, H2)
        if best_move:
            row, col = best_move
            board[row][col] = player
            change_discs(board, row, col, player)
            current_board += 1
            print("State ", current_board)
            print(f"Best move for {'Black' if player == black else 'Red'}: ({row}, {col})")
            print(f"Evaluation score for {'Red' if player == red else 'Black'}: {H2(board, player)}")
            print(f"Board after best move for {'Black' if player == black else 'Red'}:")
            display(board)
            player = 3 - player  # החלפת שחקן
        else:
            print(f"No valid moves for player {'R' if player == red else 'B'}")
            break


def H1_to_player_black_H2_to_player2():
    print("*******************************************************3**********************************************************************")
    board = beginning_board()
    player = black
    current_board = 0
    print("State ", current_board)
    display(board)
    while True:
        if player == black:
            best_move = find_best_move(board, player, H1)
        else:
            best_move = find_best_move(board, player, H2)
        if best_move:
            row, col = best_move
            board[row][col] = player
            change_discs(board, row, col, player)
            current_board += 1
            print("State ", current_board)
            print(f"Best move for {'Black' if player == black else 'Red'}: ({row}, {col})")
            if player == black:
                print(f"Evaluation score for {'Red' if player == red else 'Black'}: {H1(board, player)}")
            else:
                print(f"Evaluation score for {'Red' if player == red else 'Black'}: {H2(board, player)}")
            print(f"Board after best move for {'Black' if player == black else 'Red'}:")
            display(board)
            player = 3 - player  # החלפת שחקן
        else:
            print(f"No valid moves for player {'R' if player == red else 'B'}")
            break

def H2_to_player_black_H1_to_player2():
    print("*******************************************************3-OPOSIT**********************************************************************")
    board = beginning_board()
    player = black
    current_board = 0
    print("State ", current_board)
    display(board)
    while True:
        if player == black:
            best_move = find_best_move(board, player, H2)
        else:
            best_move = find_best_move(board, player, H1)
        if best_move:
            row, col = best_move
            board[row][col] = player
            change_discs(board, row, col, player)
            current_board += 1
            print("State ", current_board)
            print(f"Best move for {'Black' if player == black else 'Red'}: ({row}, {col})")
            if player == black:
                print(f"Evaluation score for {'Red' if player == red else 'Black'}: {H2(board, player)}")
            else:
                print(f"Evaluation score for {'Red' if player == red else 'Black'}: {H1(board, player)}")
            print(f"Board after best move for {'Black' if player == black else 'Red'}:")
            display(board)
            player = 3 - player  # החלפת שחקן
        else:
            print(f"No valid moves for player {'R' if player == red else 'B'}")
            break

# Minimax function to look two moves ahead
def minimax(board, player, depth, maximizing_player, evaluation_function):
    if depth == 0 or not any(is_valid_move(board, row, col, player) for row in range(size_of_board) for col in range(size_of_board)):
        return evaluation_function(board, player), None

    if maximizing_player:
        max_eval = -float('inf')
        best_move = None
        for row in range(size_of_board):
            for col in range(size_of_board):
                if is_valid_move(board, row, col, player):
                    board_copy = [r[:] for r in board]
                    board_copy[row][col] = player
                    change_discs(board_copy, row, col, player)
                    eval, _ = minimax(board_copy, 3 - player, depth - 1, False, evaluation_function)
                    if eval > max_eval:
                        max_eval = eval
                        best_move = (row, col)
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for row in range(size_of_board):
            for col in range(size_of_board):
                if is_valid_move(board, row, col, player):
                    board_copy = [r[:] for r in board]
                    board_copy[row][col] = player
                    change_discs(board_copy, row, col, player)
                    eval, _ = minimax(board_copy, 3 - player, depth - 1, True, evaluation_function)
                    if eval < min_eval:
                        min_eval = eval
                        best_move = (row, col)
        return min_eval, best_move
#
# A function to find the best move for the player
def find_best_move_min_max(board, player, evaluation_function):
    _, best_move = minimax(board, player, 2, True, evaluation_function)
    return best_move

#  A function for examining the evaluation functions on the original board and making the best move
def two_steps_ahead_simulation():
    print("*******************************************************4**********************************************************************")
    board = beginning_board()
    player = black
    current_board = 0
    print("State ", current_board)
    display(board)
    while True:
        best_move = find_best_move_min_max(board, player, H2)
        if best_move:
            row, col = best_move
            board[row][col] = player
            change_discs(board, row, col, player)
            current_board += 1
            print("State ", current_board)
            print(f"Best move for {'Black' if player == black else 'Red'}: ({row}, {col})")
            print(f"Evaluation score for {'Red' if player == red else 'Black'}: {H2(board, player)}")
            print(f"Board after best move for {'Black' if player == black else 'Red'}:")
            display(board)
            player = 3 - player  # Change player
        else:
            print(f"No valid moves for player {'R' if player == red else 'B'}")
            break



def main():
            board = state_whith_8_disks(8)
            print_A(board)
            print_B()
            print_C()
            test_evaluation_functionH1()
            test_evaluation_functionH2()
            H1_to_player_black_H2_to_player2()
            H2_to_player_black_H1_to_player2()
            two_steps_ahead_simulation()

if __name__ == "__main__":
    main()
