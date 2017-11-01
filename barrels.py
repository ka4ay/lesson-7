import random

barrels = [n for n in range(1, 91)]
print(barrels, end='\n')
for x in range(90, 0, -1):
    i = random.choice(barrels)
    barrels.remove(i)

    for r in range(1, 4):
        for c in range(1, 10):
            print(i, end='\t')
        print('\n')

    #print(i, x, end='\t')
