num = input("Введите число: ")
even = ''
nt_even = ''
over = 0
lenght = len(num)
i = 1
while len(even) + len(nt_even) < lenght:
    over = int(num) // (10 ** (lenght - i))
    num = int(num) - (over * (10 ** (lenght - i)))
    num = str(num)
    if over%2==0:
        over = str(over)
        even = even + over
    else:
        over = str(over)
        nt_even = nt_even + over
    over = int(over)
    i += 1
print(even)
print(nt_even)