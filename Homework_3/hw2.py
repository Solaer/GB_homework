import random

length = int(input('Введите количество эллементов: '))
num1 = []
num2 = []
i = 0
while i < length:
    num1.append(round(random.random()*100))
    i += 1
print(f'Весь массив: {num1}')
i = 0
while i < len(num1):
    if num1[i]%2 == 0:
        num2.append(num1[i])
    i += 1
print(f'Все четные эементы массива: {num2}')