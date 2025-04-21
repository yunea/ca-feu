"""Créez un programme qui remplace les caractères vides par des caractères plein pour représenter le plus grand carré possible sur un plateau.
Le plateau sera transmis dans un fichier.
La première ligne du fichier contient les informations pour lire la carte :
- nombre de lignes du plateau,
- caractères pour “vide”,
- “obstacle” et “plein”.
"""

import sys, os, re


def print_board(board):
    for line in board:
        print("".join(str(c) for c in line))


def read_file(f_name):
    raw_data = []
    with open(f_name, "r") as f:
        for line in f:
            raw_data.append([c for c in line.strip()])
    return raw_data


def get_file_name():
    if len(sys.argv) != 2:
        print(f"Error: 1 file names needed. Ex: python3 feu04.py plateau.txt")
        sys.exit()
    if not os.path.isfile(sys.argv[1]):
        print(f"Error: File does not exist")
        sys.exit()
    return sys.argv[1]


def is_file_data_valid(file):
    # Vérifie que la première ligne suit le format : "5.xo"
    s = "".join(file[0])
    match = re.match(r"(\d+)(.)(.)(.)$", s)
    if not match:
        print("Error: wrong data in first line")
        return False

    # Extraire les valeurs après validation
    nb_lines = int(match.group(1))  # Nombre de lignes du plateau
    empty_char = match.group(2)  # Caractère pour vide
    obstacle_char = match.group(3)  # Caractère pour obstacle
    full_char = match.group(4)  # Caractère pour plein

    # Vérifie qu'il y a bien nb_lines lignes restantes dans le plateau
    if len(file[1:]) != nb_lines:
        print("Error: line length incorrect")
        return False

        # Vérifie que toutes les lignes ont la même largeur
    width = len(file[1])  # Largeur de la première ligne du plateau
    for line in file[1:]:
        if len(line) != width:
            print("Error: all lines does not have same size")
            return False

        # Vérifie que tous les caractères dans la ligne sont valides
        for c in line:
            if c not in (empty_char, obstacle_char, full_char):
                print("Error: unknown char in file")
                return False

    return True


def extract_data(file):

    if not is_file_data_valid(file):
        print(f"Error : file content not valid")
        sys.exit()

    s = "".join(file[0])
    match = re.match(r"(\d+)(.)(.)(.)$", s)
    return match.group(2), match.group(3), match.group(4), file[1:]


def is_empty(board, i, j, empty_char):
    if board[i][j] == empty_char:
        return True
    return False


def get_dp(board, obstacle_char, empty_char):
    dp = []
    for row in board:
        line = []
        for _ in row:
            line.append(0)
        dp.append(line)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == obstacle_char:
                dp[i][j] = 0
            elif i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp


def get_max(dp):
    i_max = 0
    j_max = 0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j] > dp[i_max][j_max]:
                i_max = i
                j_max = j

    return i_max, j_max, dp[i_max][j_max]


def get_new_board(i_max, j_max, v_max, board, full_char):
    for i in range(v_max):
        for j in range(v_max):
            board[i_max - i][j_max - j] = full_char
    return board


def main():
    f_board = get_file_name()
    file = read_file(f_board)

    empty_char, obstacle_char, full_char, board = extract_data(file)

    dp = get_dp(board, obstacle_char, empty_char)
    i_max, j_max, v_max = get_max(dp)
    result = get_new_board(i_max, j_max, v_max, board, full_char)

    print_board(result)


if __name__ == "__main__":
    main()
