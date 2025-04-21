# Créez un programme qui trouve et affiche la solution d’un Sudoku.

import sys, os


def print_sudoku(board):
    for line in board:
        print("".join(line))


def read_sudoku(f_name):
    board = []
    with open(f_name, "r") as f:
        for line in f:
            board.append([c for c in line if c != "\n"])
    return board


def get_file_name():
    if len(sys.argv) != 2:
        print(f"Error: 1 file names needed. Ex: python3 feu03.py sudoku.txt")
        sys.exit()
    if not os.path.isfile(sys.argv[1]):
        print(f"Error: File does not exist")
        sys.exit()
    return sys.argv[1]


def is_unit_valid(unit):
    seen = set()
    for num in unit:
        if num != ".":
            if num in seen:
                return False  # doublon trouvé
            seen.add(num)
    return True


def is_board_valid(board):
    # vérifie les dimensions
    if len(board) != 9:
        return False
    for row in board:
        if len(row) != 9:
            return False
        # vérifie les valeurs
        for val in row:
            if val not in "123456789.":
                return False

    # vérifie les doublons dans les lignes
    for row in board:
        if not is_unit_valid(row):
            return False

    # vérifie les doublons dans les colonnes
    for col_idx in range(9):
        col = []
        for row_idx in range(9):
            col.append(board[row_idx][col_idx])
        if not is_unit_valid(col):
            return False

        # vérifie les doublons dans les régions 3x3
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                square = [
                    board[r][c]
                    for r in range(box_row, box_row + 3)
                    for c in range(box_col, box_col + 3)
                ]
                if not is_unit_valid(square):
                    return False

    return True


def find_empty_case(board):
    for row_idx in range(len(board)):
        for column_idx in range(len(board[0])):
            if board[row_idx][column_idx] == ".":
                return row_idx, column_idx
    return None


def is_valid(board, row, column, num):
    # vérification de la ligne (row)
    if num in board[row]:
        return False
    # vérification de la colonne (column)
    for i in range(len(board[0])):
        if board[i][column] == num:
            return False
    # vérification de la région
    region_row = row // 3
    region_col = column // 3
    for i in range(region_row * 3, region_row * 3 + 3):
        for j in range(region_col * 3, region_col * 3 + 3):
            # Tu accèdes à chaque cellule de la région
            if board[i][j] == num:
                return False
    return True


def solve_sudoku(board):
    empty = find_empty_case(board)
    if not empty:
        return True

    row_idx, column_idx = empty

    for num in "123456789":
        if is_valid(board, row_idx, column_idx, num):
            board[row_idx][column_idx] = num

            if solve_sudoku(board):
                return True

            board[row_idx][column_idx] = "."

    return False


def main():
    f_sudoku = get_file_name()
    sudoku_board = read_sudoku(f_sudoku)

    if not is_board_valid(sudoku_board):
        print("Error: Invalid Sudoku board")
        sys.exit()

    solve_sudoku(sudoku_board)
    print_sudoku(sudoku_board)


if __name__ == "__main__":
    main()
