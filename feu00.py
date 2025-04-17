# Échauffement
# Créez un programme qui affiche un rectangle dans le terminal.

import sys

# ligne de début et de fin 
def line(arg) : 
  i = 0
  match arg : 
    case 1 : 
      return "o"
    case 2 : 
      return "oo"
    case _ : 
      s = "o"
      while i < arg-2 : 
        s += "-"
        i += 1
      s += "o"
      return s

# ligne du centre
def center_line(arg) :
  i = 0
  match arg : 
    case 1 : 
      return "|"
    case 2 : 
      return "||"
    case _ : 
      s = "|"
      while i < arg-2 : 
        s += " "
        i += 1
      s += "|"
      return s

# définition du rectangle dans une liste 
def list_rectangle(arg1, arg2) : 
  i = 0
  rows = []
  match arg2 : 
    case 1 : 
      rows.append(line(arg1))
      return rows
    case 2 : 
      rows.append(line(arg1))
      rows.append(line(arg1))
      return rows
    case _ : 
      # ajout de la première ligne
      rows.append(line(arg1))
      while i < arg2-2 : 
        # ajout des lignes au centre
        rows.append(center_line(arg1))
        i += 1
      # ajout de la dernière ligne
      rows.append(line(arg1))
      return rows

# affichage du rectangle
def display(rectangle) : 
  for item in rectangle : 
    print(item)


# Les règles 
# 1. La liste d'argument = 3 (nom du fichier, arg1, arg2)
# 2. Les arguments sont des entiers
# 3. Les arguments sont > 0

def check_argv(argv_list) :
  if len(argv_list) == 3 : 
    if argv_list[1].isdigit() and argv_list[2].isdigit() : 
      if int(argv_list[1])==0 or int(argv_list[2])==0 :
        return False, "Error : arguments must be greater than 0"
      else : 
        return True, ""
    else : 
      return False, "Error : arguments must be numbers"
  else :
    return False, "Error : must have 2 arguments"


# ----------- main -----------
good_args, error_message = check_argv(sys.argv)
if good_args : 
  columns = int(sys.argv[1])
  rows = int(sys.argv[2])
  rectangle = list_rectangle(columns, rows)
  display(rectangle)
else :
  print(error_message)
