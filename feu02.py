# Trouver une forme
# Créez un programme qui affiche la position de l’élément le plus en haut à gauche (dans l’ordre) d’une forme au sein d’un plateau.

def print_board(board) : 
  for line in board : 
    print(*line)


def build_display_grid(board, to_find, start_i, start_j) : 
  rows = len(board)
  columns = len(board[0])

  new_board = []

  for i in board : 
    line = []
    for j in i : 
      line.append("-")
    new_board.append(line)

  for di in range(len(to_find)):
    for dj in range(len(to_find[0])):
        if to_find[di][dj] != " ":
            new_board[start_i + di][start_j + dj] = to_find[di][dj]

  print_board(new_board)


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

def main() : 
  board = [[0,0,0,0],[1,1,1,1],[2,3,3,1]]
  to_find = [[1, 1], [" ", 1]]
  unfindable = [[0,0], [0,0]]

  is_found, i , j = match_found(board, to_find)
  if is_found : 
    print(f"Trouvé !\nCoordonnées : {i}, {j}")
    build_display_grid(board, to_find, i, j)
  else : 
    print(f"Introuvable")


main()
