"""
Coding Accelerator - Échauffement
Créez un programme qui affiche un rectangle dans le terminal.
"""


import sys

def line(width) : 
  """Retourne une ligne horizontale avec les coins et les bordures en caractères."""
  if width == 1 : return "o"
  else : return "o" + "-" * (width - 2) + "o"

def center_line(width) :
  """Retourne une ligne centrale du rectangle avec bords verticaux et espace intérieur."""
  if width == 1 : return "|"
  else : return "|" + " " * (width - 2) + "|"

def list_rectangle(width, height) : 
  """Construit le rectangle sous forme de liste de chaînes, ligne par ligne."""
  if height == 1:
    return [line(width)]
  elif height == 2:
    return [line(width), line(width)]
  else:
    return [line(width)] + [center_line(width) for _ in range(height - 2)] + [line(width)]

# affichage du rectangle
def display(rectangle) : 
  for item in rectangle : 
    print(item)


def check_argv(argv_list):
    """
    Vérifie que les arguments sont valides :
    - exactement 2 arguments (en plus du nom du script)
    - entiers strictement positifs
    Retourne (True, "") si OK, sinon (False, message d'erreur)
    """
    if len(argv_list) != 3:
        return False, "Error: must have 2 arguments"

    try:
        width = int(argv_list[1])
        height = int(argv_list[2])
    except ValueError:
        return False, "Error: arguments must be integers"

    if width <= 0 or height <= 0:
        return False, "Error: arguments must be greater than 0"

    return True, ""
  

def main() :
  good_args, error_message = check_argv(sys.argv)
  if good_args : 
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    rectangle = list_rectangle(width, height)
    display(rectangle)
  else :
    print(error_message)



if __name__ == "__main__":
    main()
