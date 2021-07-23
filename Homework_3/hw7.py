import random

lenght = int(input('Введите количество эллементов массива: '))
num = []
i = 0
while i < lenght:
    num.append(round(random.random()*100))
    i += 1
print(num)
i = 0
min1 = min(num)
print(min(num))
num.remove(min1)
min2 = min(num)
if min2 == min1:
    print(min1)
else:
    print(min2)