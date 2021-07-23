num = int(input('Введите целое числа (как закончите введите 0): '))
num1 = 0
num2 = 0
while num != 0:
    max = num
    max_sum = 0
    while num > 0:
        max_sum = max_sum + num%10
        num = num // 10
    if max_sum > num1:
        num1 = max_sum
        num2 = max
    num = int(input())
print(f'Большим числом {num2} т.к. имеет самую большую сумму цифр: {num1}')
