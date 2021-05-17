import random
ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
choose = int(input("Выберете что вы какой рандомайзер вам нужен: \n(1) Цельные числа числа \n(2) Вещественные числа \n(3) Случайный символ английского алфавита\n"))
if choose == 1:
    a = int(input('Введите ограничение на первое ЦЕЛЬНОЕ ЧИСЛО: '))
    b = int(input('Введите ограничение на второе ЦЕЛЬНОЕ ЧИСЛО: '))
    print(f"{random.randint(a, b)}")
elif choose == 2:
    a = float(input('Введите ограничение на первое ЧИСЛО: '))
    b = float(input('Введите ограничение на второе ЧИСЛО: '))
    с = int(input("Введите количество чисел после запятой: "))
    print(f"{round(random.uniform(a, b), с)}")
elif choose == 3:
    let1 = int(ABC.index(input("Введите МАЛЕНЬКУЮ БУКВУ ЛАТИНСКОГО алфавита: "))) + 1
    let2 = int(ABC.index(input("Введите МАЛЕНЬКУЮ БУКВУ ЛАТИНСКОГО алфавита: "))) + 1
    let = random.randint(let1, let2) - 1
    print(ABC[let])
else:
    print("Извените я вас не понял")
