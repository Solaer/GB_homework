import random

length = int(input('Введите количество эллементов массива: '))
num = []
num1 = 0
pos1 = 0
num2 = 100
pos2 = 0
i = 0
while i < length:
    num.append(round(random.random()*100))
    i += 1
print(f'Оригинальный массив: {num}')
i = 0
while i < len(num):
    if num[i] > num1:
        num1 = num[i]
        pos1 = i
    i += 1
print(f'Самое большое число в массиве: {num1}')
i = 0
while i < len(num):
    if num[i] < num2:
        num2 = num[i]
        pos2 = i
    i += 1
print(f'Самое мальенкое число в массиве: {num2}')
num[pos1] = num2
num[pos2] = num1
print(f'Измененный массив: {num}')