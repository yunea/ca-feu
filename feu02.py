# Trouver une forme
# Créez un programme qui affiche la position de l’élément le plus en haut à gauche (dans l’ordre) d’une forme au sein d’un plateau.

board = [[0,0,0,0],[1,1,1,2],[2,3,3,4]]
to_find = [[1,2], [3,4]]
unfindable = [[0,0], [0,0]]


for line in board : 
  print(*line)

print("-------------")

for line in to_find : 
  print(*line)

print("-------------")

i = 0
j = 0
di = 0
dj = 0

match = False

for i in range(len(board)) : # rows
  for j in range(len(board[0])) : # columns
    print("pr indx", i, j, di, dj)
    if board[i][j] == to_find[di][dj] :
      print("premier chiffre similaire")
      print("pr map", board[i][j], to_find[di][dj])

      for di in range(len(to_find)) :
        for dj in range(len(to_find[0])) :
          if i + di < len(board) and j + dj < len(board[0]):
            print("nv idx", i, j, di, dj)
            if board[i + di][j+dj] == to_find[di][dj] :
              print("nouveau match")
              print("nv map", board[i][j], to_find[di][dj])
              match = True
            else : 
              di = 0
              dj = 0
              match = False

print("MATCH : ", match)
      
