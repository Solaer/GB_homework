num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
num3 = int(input("Введит етреттье число"))
if (num1 > num2 and num3 > num1) or (num1 > num3 and num2 > num1):
    print(f'Средним числом явлеться {num1}')
elif (num2 > num3 and num1 > num2) or (num2 > num1 and num3 > num2):
    print(f'Средним числом явлеться {num2}')
elif (num3 > num1 and num2 > num3) or (num3 > num2 and num1 > num3):
    print(f'Средним числом явлеться {num3}')