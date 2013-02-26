import random

c = 0
n = 10000000
for i in range(n):
    x = random.random()
    y = random.random()
    if x**2 + y**2 < 1:
        c += 1

print c/float(n) * 4