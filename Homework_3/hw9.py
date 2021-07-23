from random import random

m = 10
n = 5
a = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(int(random()*100))
        print("%3d" % b[j], end=" ")
    a.append(b)
    print("|")
for i in range(m):
    print(" --", end=" ")
print()

less = 1000
less_i = 0
for i in range(m):
    s = 0
    for j in range(n):
        s = s + a[j][i]
    print("%3d" % s, end=" ")
    if less > s:
        less = s
        less_i = i
print()
bigger = 0
for j in range(n):
    if a[j][less_i] > bigger:
        bigger = a[j][less_i]
print(f"Саммый большой эллемент в самом малельком столбце {less_i + 1} со значением {less} явлеться: {bigger}")
