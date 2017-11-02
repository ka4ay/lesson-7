import random

numbers = [n for n in range(1, 91)]
row = []

for x in range(1, 16):
    i = random.choice(numbers)
    numbers.remove(i)
    row.append(i)

print(sorted(row))



#print(numbers)
#print(i, x)