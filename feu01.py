# Évaluer une expression
# Créez un programme qui reçoit une expression arithmétique dans une chaîne de caractères et en retourne le résultat après l’avoir calculé.
# Vous devez gérer les 5 opérateurs suivants : “+” pour l’addition, “-” pour la soustraction, “*” la multiplication, “/” la division et “%” le modulo.

import sys

# Transforme une liste de chaînes en float ou conserve les opérateurs
def str_to_tokens(input_expr):
  elements = input_expr.replace(" ", "")
  tokens = []
  num = ""
  for elem in elements:
    if elem in "/*%-+()." or elem.isdigit():  # On autorise les opérateurs et chiffres
      if elem in "+-*/%()":  # Si on rencontre un opérateur
        if num:  # Si num n'est pas vide, on ajoute le nombre précédant l'opérateur
          tokens.append(float(num))
          num = ""  # Réinitialiser le num après avoir ajouté
          tokens.append(elem)  # Ajouter l'opérateur
        elif elem == ".":  # Si on rencontre un point décimal
          if num and num.count(".") == 0:  # Vérifier qu'il n'y a pas déjà un point dans num
            num += elem
          else:
            raise ValueError("Erreur : Le nombre contient plusieurs points décimaux.")
        else : 
          tokens.append(elem)
      else:  # Ajoute les chiffres à num
        num += elem
    else:
      raise ValueError(f"Caractère non reconnu : '{elem}'. Seuls les opérateurs et les chiffres sont autorisés.")
    
  # Après la boucle, s'il y a un numéro restant dans num, on l'ajoute à tokens
  if num:
    try:
      tokens.append(float(num))  # Essayer de convertir num en float
    except ValueError:
      raise ValueError(f"Erreur : '{num}' n'est pas un nombre valide.")
  return tokens

# Calcule l'opération entre deux nombres
def handle_operation(op, num1, num2):
  if op == "*": return num1 * num2
  elif op == "/": return num1 / num2
  elif op == "%": return num1 % num2
  elif op == "+": return num1 + num2
  elif op == "-": return num1 - num2

# Gère *, / et %
def priority_operation(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] in ["*", "/", "%"]:
            result = handle_operation(tokens[i], tokens[i - 1], tokens[i + 1])
            tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
            i = 0  # reset après modification de la liste
        else:
            i += 1
    return tokens

# Gère + et -
def secondary_operation(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] in ["+", "-"]:
            result = handle_operation(tokens[i], tokens[i - 1], tokens[i + 1])
            tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
            i = 0  # reset après modification
        else:
            i += 1
    return tokens

# Remplace les sous-expressions entre parenthèses par leur résultat
def evaluate_parentheses(tokens):
    while ")" in tokens:
        # Trouve la parenthèse ouvrante la plus profonde
        open_idx = 0
        for i in range(len(tokens)):
            if tokens[i] == "(":
                open_idx = i
        close_idx = tokens.index(")")
        sub_expr = tokens[open_idx + 1:close_idx]
        result = evaluate(sub_expr)
        tokens = tokens[:open_idx] + [result] + tokens[close_idx + 1:]
    return tokens

# Fonction principale de calcul
def evaluate(tokens):
    tokens = evaluate_parentheses(tokens)
    tokens = priority_operation(tokens)
    tokens = secondary_operation(tokens)
    return tokens[0]

# Lancement du programme
def main():
    input_expr = sys.argv[1]
    token_list = str_to_tokens(input_expr)
    result = evaluate(token_list)
    print(result)

if __name__ == "__main__":
  main()
