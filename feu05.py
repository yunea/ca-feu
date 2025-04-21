"""Créez un programme qui trouve le plus court chemin entre l’entrée et la sortie d’un labyrinthe en évitant les obstacles.
Le labyrinthe est transmis en argument du programme. La première ligne du labyrinthe contient les informations pour lire la carte :
LIGNESxCOLS, caractère plein, vide, chemin, entrée et sortie du labyrinthe.
Le but du programme est de remplacer les caractères “vide” par des caractères “chemin” pour représenter le plus court chemin pour traverser le labyrinthe.
Un déplacement ne peut se faire que vers le haut, le bas, la droite ou la gauche.
"""

import sys, os, re


# Affiche le labyrinthe ligne par ligne
def print_board(board):
    for line in board:
        print("".join(str(c) for c in line))


# Vérifie la validité des arguments en ligne de commande
def check_arguments(args):
    if len(args) != 2:
        print(f"Error: 1 argument needed")
        sys.exit()
    if not os.path.exists(sys.argv[1]):
        print(f"Erreur : Le fichier {sys.argv[1]} n'existe pas.")
        sys.exit()
    if not os.path.isfile(args[1]):
        print(f"Error: {args[1]} is not a file")
        sys.exit()


# Lit le contenu du fichier labyrinthe et le retourne sous forme de liste
def read_file(f_name):
    f_content = []
    with open(f_name, "r") as f:
        for line in f:
            f_content.append([c for c in line.strip()])
    return f_content


# Analyse les données du fichier et extrait les infos utiles
def get_data(content):
    # Extraire la première ligne
    header_line = "".join(content[0])
    match = re.match(r"^(\d+)x(\d+)(.{5})$", header_line)
    # Valider les arguments de la première ligne
    if not match:
        print("Error: wrong data in first line.")
        sys.exit()

    # Extraire les arguments
    rows = int(match.group(1))
    columns = int(match.group(2))
    full_char = match.group(3)[0]
    empty_char = match.group(3)[1]
    road_char = match.group(3)[2]
    in_char = match.group(3)[3]
    out_char = match.group(3)[4]

    # Valider le nombre de lignes
    if len(content[1:]) != rows:
        print(
            f"Error: number of lines incorrect. Should be {rows} but is {len(content[1:])}."
        )
        sys.exit()

    # Valider le nombre de colonnes
    for line in content[1:]:
        if len(line) != columns:
            print(
                f"Error: number of columns incorrect. Should be {columns} but is {len(line)}."
            )
            sys.exit()

    # Valider le contenu du plateau (pas de caractère inconnu présent)
    for line in content[1:]:
        for char in line:
            if not char in [full_char, empty_char, road_char, in_char, out_char]:
                print(f"Error: unknown char ({char}) in file.")
                sys.exit()

    return {
        "full": full_char,
        "empty": empty_char,
        "road": road_char,
        "in": in_char,
        "out": out_char,
        "board": content[1:],
    }


# Retourne la position (ligne, colonne) d’un caractère donné dans la grille
def get_position(char, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == char:
                return int(i), int(j)


# Calcule et trace le plus court chemin entre entrée et sortie
def find_shortest_path(data):
    in_pos = get_position(data["in"], data["board"])
    out_pos = get_position(data["out"], data["board"])
    board = data["board"]
    board[in_pos[0]][in_pos[1]] = 1

    directions = [(-1, 0), (+1, 0), (0, +1), (0, -1)]  # haut, bas, droite, gauche

    queue = []
    queue.append((in_pos[0], in_pos[1]))

    while queue:
        i = queue[0][0]
        j = queue[0][1]
        current = int(board[i][j])
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                if (
                    board[ni][nj] == data["empty"]
                    or isinstance(board[ni][nj], int)
                    and board[ni][nj] > current + 1
                ):
                    board[ni][nj] = current + 1
                    queue.append((ni, nj))
        queue.pop(0)

    # Récupérer la case avant la sortie (avec le nb le plus petit)
    i = out_pos[0]
    j = out_pos[1]
    min_distance = len(board) * len(board[0])
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
            if isinstance(board[ni][nj], int) and board[ni][nj] < min_distance:
                min_distance = int(board[ni][nj])
                board[ni][nj] = data["road"]
                i = ni
                j = nj

    # À partir de cette case, je remonte le chemin
    current = min_distance
    while current != 1:
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                if board[ni][nj] == int(current) - 1:
                    board[ni][nj] = data["road"]
                    i = ni
                    j = nj
                    current -= 1

    # clean board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not board[i][j] in [data["full"], data["road"]]:
                board[i][j] = " "

    board[in_pos[0]][in_pos[1]] = data["in"]
    board[out_pos[0]][out_pos[1]] = data["out"]

    return board


def main():
    check_arguments(sys.argv)
    f_content = read_file(sys.argv[1])
    data = get_data(f_content)
    result = find_shortest_path(data)
    print_board(result)


if __name__ == "__main__":
    main()
