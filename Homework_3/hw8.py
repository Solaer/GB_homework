m = 5
n = 4
a = []
num = 0
for i in range(n):
    b = []
    for j in range(m):
        num = (input(f"Введите {j + 1} элемент строки {i + 1}:"))
        if num == '':
            num = 0
        num = int(num)
        b.append(num)

    a.append(b)

for i in range(n):
    print(a[i],"   |", sum(a[i]))
