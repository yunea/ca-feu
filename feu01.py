# Évaluer une expression
# Créez un programme qui reçoit une expression arithmétique dans une chaîne de caractères et en retourne le résultat après l’avoir calculé.
# Vous devez gérer les 5 opérateurs suivants : “+” pour l’addition, “-” pour la soustraction, “*” la multiplication, “/” la division et “%” le modulo.

import sys 

def str_to_float(calcul) :
  new_list = []
  for item in calcul:
    if item in ["*", "/", "%", "+", "-", "(", ")"]: new_list.append(item)
    else : new_list.append(float(item))
  return new_list


def handle_operation(op, num1, num2) : 
  num1 = float(num1)
  num2 = float(num2)
  if op == "*" : return num1 * num2
  elif op == "/" : return num1 / num2
  elif op == "%" : return num1 % num2
  elif op == "+" : return num1 + num2
  elif op == "-" : return num1 - num2
   

def priority_operation(tokens):
  i = 0
  while i < len(tokens):
    if tokens[i] in ["*", "/", "%"]:
      result = handle_operation(tokens[i], tokens[i - 1], tokens[i + 1]) 
      # remplace les 3 éléments (num1 op num2) par le résultat
      tokens = tokens[:i - 1] + [result] + tokens[i + 2:]
      i = 0  # recommence au début car la liste a changé
    else:
      i += 1
  return tokens


def secondary_operation(arg) :
  i = 0
  while i < len(arg) : 
    if arg[i] in ["+", "-"] :
      result = handle_operation(arg[i], arg[i - 1], arg[i + 1])
      arg = arg[:i-1] + [result] + arg[i+2:]
      i = 0
    else : 
      i += 1
  return arg


def evaluate_parentheses(tokens) : 
  while ")" in tokens :
    open_idx = 0
    i = 0
    for i in range(len(tokens)) :
      if tokens[i] == "(" :
        open_idx = i
    close_idx = tokens.index(")")
    parenthese_list = tokens[open_idx+1:close_idx]
    result = evaluate(parenthese_list)
    tokens = tokens[:open_idx] + [result] + tokens[close_idx+1:]
  return tokens
  
def evaluate(tokens):
  tokens = evaluate_parentheses(tokens)
  tokens = priority_operation(tokens)
  tokens = secondary_operation(tokens)
  return tokens[0]
  

def main() : 
  tokens = str_to_float(sys.argv[1].split())
  result = evaluate(tokens)
  print(result)


main()