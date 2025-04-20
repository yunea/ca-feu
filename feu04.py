"""Créez un programme qui remplace les caractères vides par des caractères plein pour représenter le plus grand carré possible sur un plateau.
Le plateau sera transmis dans un fichier.
La première ligne du fichier contient les informations pour lire la carte : 
- nombre de lignes du plateau, 
- caractères pour “vide”, 
- “obstacle” et “plein”.
"""

import sys, os, re


def print_board(board) : 
	for line in board : 
		print("".join(line))


def read_file(f_name):
	board = []
	with open(f_name, "r") as f:
		for line in f:
			board.append([c for c in line if c != '\n'])
	return board


def get_file_name() : 
	if len(sys.argv) != 2 : 
		print(f"Error: 1 file names needed. Ex: python3 feu04.py plateau.txt")
		sys.exit()
	if not os.path.isfile(sys.argv[1]) : 
		print(f"Error: File does not exist")
		sys.exit()
	return sys.argv[1]

def is_file_data_valid(file) :

	# Vérifie que la première ligne suit le format : "5.xo"
  match = re.match(r"(\d+)(.)(.)(.)$", file[0])
  if not match : return False
	
	# Extraire les valeurs après validation
  nb_lines = int(match.group(1))  # Nombre de lignes du plateau
  empty_char = match.group(2)  # Caractère pour vide
  obstacle_char = match.group(3)  # Caractère pour obstacle
  full_char = match.group(4)  # Caractère pour plein
	
	# Vérifie qu'il y a bien nb_lines lignes restantes dans le plateau
  if len(file[1:]) != nb_lines : return False

  # Vérifie que toutes les lignes ont la même largeur
  width = len(file[1])  # Largeur de la première ligne du plateau
  for line in file[1:]:
    if len(line) != width:
      return False
  # Vérifie que tous les caractères dans la ligne sont valides
    for c in line:
      if c not in (empty_char, obstacle_char, full_char):
        return False
			
  return True


def extract_data(file) : 
	data = file[0]
	file.pop(0)
	return data[0], data[1], data[2], data[3], file


def main() : 
	f_board = get_file_name()
	file = read_file(f_board)

	lines, empty_char, obstacle_char, filled_char, board = extract_data(file)
	print_board(file)


if __name__ == "__main__":
	main()