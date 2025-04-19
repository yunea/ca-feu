# Trouver une forme
# Créez un programme qui affiche la position de l’élément le plus en haut à gauche (dans l’ordre) d’une forme au sein d’un plateau.

import sys, os

def print_board(board) : 
  for line in board : 
    print(*line)


def build_display_grid(board, to_find, start_i, start_j) : 
  rows = len(board)
  columns = len(board[0])

  new_board = []
  new_board = [["-" for _ in row] for row in board]

  for di in range(len(to_find)):
    for dj in range(len(to_find[0])):
        if to_find[di][dj] != " ":
            new_board[start_i + di][start_j + dj] = to_find[di][dj]
  return new_board


def match_form(board, to_find, i, j) :
  for di in range(len(to_find)) :
    for dj in range(len(to_find[0])) :
      if i + di >= len(board) or j + dj >= len(board[0]):
        return False
      if to_find[di][dj] != " " and board[i + di][j+dj] != to_find[di][dj] :
        return False
  return True


def match_found(board, to_find) :
  for i in range(len(board)) : # rows
    for j in range(len(board[0])) : # columns
      if match_form(board, to_find, i, j) : 
        
        return True, i, j
  return False, None, None

def get_file_data(f_name):
    board = []
    with open(f_name, "r") as f:
        for line in f:
            board.append([c for c in line if c != '\n'])
    return board

def get_file_name() : 
  if len(sys.argv) != 3 : 
    print(f"Error: 2 file names needed. Ex: python3 feu02.py board.txt to_find.txt")
    sys.exit()
  if not os.path.isfile(sys.argv[1]) or not os.path.isfile(sys.argv[2]) : 
    print(f"Error: File does not exist")
    sys.exit()
  return sys.argv[1], sys.argv[2]

def main() : 
  f_board, f_to_find = get_file_name()

  board = get_file_data(f_board)
  to_find = get_file_data(f_to_find)

  is_found, i , j = match_found(board, to_find)
  if is_found : 
    print(f"Trouvé !\nCoordonnées : {i}, {j}")
    new_board = build_display_grid(board, to_find, i, j)
    print_board(new_board)
  else : 
    print(f"Introuvable")


main()
