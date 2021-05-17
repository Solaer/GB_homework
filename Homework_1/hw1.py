num = input("Введите трех значное число: ")
num2 = list(num)
if len(num2) == 3:
    sum = int(num2[0]) + int(num2[1]) + int(num2[2])
    mul = int(num2[0]) * int(num2[1]) * int(num2[2])
    print(f"Сумма всех цифр равна: {sum}. Произведени всех цифр равна: {mul}")
elif len(num2) > 3:
    print('вы ввели слишком большое число')
else:
    print('Вы ввели слишком маленкое число')
