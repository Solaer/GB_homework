import random

el = int(input("Введите количество эллементов: "))
num = 0
even = ''
nt_even = ''
i = 0
while i < el:
    num = round(random.random()*100)
    if num%2 == 0:
        num = str(num)
        even = even + num + ', '
    else:
        num = str(num)
        nt_even = nt_even + num + ', '
    num = int(num)
    i += 1

print(f'Четные {even}')
print(f'Не четные {nt_even}')