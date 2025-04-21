import sys
import random

if len(sys.argv) < 4 or len(sys.argv[3]) < 5:
    print("params needed: height width characters")
else:
    height = int(sys.argv[1])
    width = int(sys.argv[2])
    chars = sys.argv[3]
    gates = int(sys.argv[4]) if len(sys.argv) > 4 else 0  # optionnel

    entry = random.randint(2, width - 3)
    entry2 = random.randint(2, width - 3)

    print(f"{height}x{width}{chars}")

    for y in range(height):
        for x in range(width):
            if y == 0 and x == entry:
                print(chars[3], end="")
            elif y == height - 1 and x == entry2:
                print(chars[4], end="")
            elif (
                1 <= y <= height - 2
                and 1 <= x <= width - 2
                and random.randint(0, 99) > 20
            ):
                print(chars[1], end="")
            else:
                print(chars[0], end="")
        print()
