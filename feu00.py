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


def parse_args(argv):
  if len(argv) != 3:
      raise ValueError("Must provide exactly 2 arguments")
    
  width = int(argv[1])
  height = int(argv[2])

  if width <= 0 or height <= 0:
      raise ValueError("Arguments must be greater than 0")

  return width, height
  

def main() :
  try:
    width, height = parse_args(sys.argv)
    rectangle = list_rectangle(width, height)
    display(rectangle)
  except Exception as e:
    print(f"Error: {e}")



if __name__ == "__main__":
  main()
