import random

length = int(input('Введите количество эллементов массива: '))
num = []
i = 0
while i < length:
    num.append(round(random.random()*100))
    i += 1
print(f'Оригинальный массив: {num}')
number = set(num)
x = 0
numb = []
for x in number:
    numb.append(x)
max_i = 0
max = 0
rep = 0
i = 0
c = 0
while True:
    if numb[c] == num[i]:
        rep += 1
    i += 1
    if i == len(num):
        if max < rep:
            max = rep
            max_i = numb[c]
        c += 1
        i = 0
        rep = 0
    if c == len(numb):
        break
if max == 1:
    print('Все числа встречаються одни раз')
else:
    print(f'Число {max_i} встречаеться всего {max} раз.')