def calculatid (num1, num2, doit):
    if doit == "+":
        res = num1 + num2
        print(res)
    if doit == "-":
        res = num1 - num2
        print(res)
    if doit == "*":
        res = num1 * num2
        print(res)
    if doit == "/":
        res = num1 / num2
        print(res)


while True:
    num1 = int(input("Введите первое число: "))
    doit = input("Введите действие: ")
    if  doit != "+" and doit != "-" and doit != "*" and doit != "/":
        print("Невозможно выполнить действие")
        continue
    if doit == "0":
        print("Спасибо за то что воспользовалиь моим калькулятора")
        break
    num2 = int(input("Введите второе число: "))
    if num2 == 0:
        res = input("Вы уверены что хотите схлопнуть вселенную\nНажмите да(Y) или нет (N): ")
        if res == 'Y' or res == 'y':
            print("Передал ваши координаты TVA. Пожалуйста не сопротивляйтесь.")
            continue
        else:
            print("Насей раз прошаем, но в следующий раз не допускайте подобной ситуации")
            continue
    calculatid(num1, num2, doit)