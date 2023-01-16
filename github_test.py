import random

a = random.randrange(1, 101)
b = random.randrange(1, 11)

f = ""

for i in range(a):
    if i % b == 0:
        f = f + " "
    else:
        f = f + "-"
print(f)