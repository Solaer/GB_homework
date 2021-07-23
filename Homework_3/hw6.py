import random

num = []
length = int(input('Введите количество эллементов массива: '))
i = 0
while i < length:
    num.append(round(random.random()*100))
    i += 1
print(num)
min = 100
min_i = 0
max = 0
max_i = 0
i = 0
while i < length:
    if min > num[i]:
        min = num[i]
        min_i = i
    if max < num[i]:
        max = num[i]
        max_i = i
    i += 1
print(f'Минимальное число: {min}, на позиции: {min_i}')
print(f'Максимальное число: {max}, на позиции: {max_i}')
if max_i > min_i:
    print(f'Сумма между минимальными и максимальными элементами массива: {sum(num[min_i:max_i]) - min}')
elif min_i > max_i:
    print(f'Сумма между минимальными и максимальными элементами массива: {sum(num[max_i:min_i]) - max}')