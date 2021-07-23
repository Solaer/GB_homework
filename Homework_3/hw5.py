import random

length = int(input('Введите количество эллементов массива: '))
num = []
i = 0
while i < length:
    num.append(round(random.random()*-100))
    i += 1
print(num)
i = 0
min = 0
min_i = 0
while i < length:
    if min > num[i]:
        min = num[i]
        min_i = i
    i += 1
print(f'Саммым маленьким числом являеться: {min}. На позиции: {min_i}')
