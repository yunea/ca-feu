# Trouver le plus grand carré : annexe

import sys
import random

if len(sys.argv) != 4:
    print("params needed: x y density")
    sys.exit()

x = int(sys.argv[0 + 1])  # sys.argv[0] est le nom du script
y = int(sys.argv[1 + 1])
density = int(sys.argv[2 + 1])

print(f"{y}.xo")

for i in range(y + 1):
    for j in range(x + 1):
        char = 'x' if random.randint(0, y - 1) * 2 < density else '.'
        print(char, end='')
    print()