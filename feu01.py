# Évaluer une expression
# Créez un programme qui reçoit une expression arithmétique dans une chaîne de caractères et en retourne le résultat après l’avoir calculé.
# Vous devez gérer les 5 opérateurs suivants : “+” pour l’addition, “-” pour la soustraction, “*” la multiplication, “/” la division et “%” le modulo.

import sys 

def priority_calculation(arg) : 
  res = 0
  i = 0
  while i < len(arg) : 
    #print(arg, arg[i])
    match arg[i] :
      case "*" : 
        res = int(arg[i-1]) * int(arg[i+1])
        arg[i] = str(res)
        arg.pop(i+1)
        arg.pop(i-1)
        i -= 1
      case "/" :
        res = int(arg[i-1]) / int(arg[i+1])
        arg[i] = res
        arg.pop(i+1)
        arg.pop(i-1)
        i -= 1
      case "%":
        res = int(arg[i-1]) % int(arg[i+1])
        arg[i] = res
        arg.pop(i+1)
        arg.pop(i-1)
        i -= 1
    i += 1
  return arg

def secondary_calculation(arg) :
  res = 0
  i = 0
  for item in arg : 
    #print( arg, item)
    match item :
      case "+" :
        res = int(arg[i-1]) + int(arg[i+1])
        arg[i+1] = res
      case "-" : 
        res = int(arg[i-1]) - int(arg[i+1])
        arg[i+1] = res
    i += 1
  return(arg[i-1])

res1 = priority_calculation(sys.argv[1].split())
res2 = secondary_calculation(res1)
print(res2)