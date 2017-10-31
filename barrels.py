import random

barrels = [n for n in range(1, 91)]
print(barrels)
for x in range(90, 0, -1):
    i = random.choice(barrels)
    barrels.remove(i)

    print(i, x)
