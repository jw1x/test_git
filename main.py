import random

x = [random.randint(1, 100) for i in range(100)]

for i in range(len(x)-1):
    if x[i] > x[i+1]:
        print(f"{x[i]}(сосед {x[i+1]})")
