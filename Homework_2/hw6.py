import random

guess = 0
b = int(input("Пожалуйста выберете уровень сложность."
              "\n   Введиет цифру чтобы выбрать уровень сложности"
              "\n0. Папуль можно поиграть?(20 попыток)"
              "\n1. Легкий уровень сложности(10 попыток)"
              "\n2. Нормальная сложность(8 попыток)"
              "\n3. Сложно(6 попыток)"
              "\n4. Ещё сложнее(5 попыток)"
              "\n5. Я Экстрасенс(3 попытки)"
              "\n6. Пошады не будет одна ошибка и ты труп (1 попытка)"
              "\n: "))
if b == 1:
    Try = 10
elif b == 2:
    Try = 8
elif b == 3:
    Try = 6
elif b == 4:
    Try = 5
elif b == 5:
    Try = 3
elif b == 6:
    Try = 1
elif b == 0:
    Try = 20
a = random.randint(1, 100)
while True:
    print(f"У вас попыток осталоьс: {Try}")
    guess = int(input("Это число: "))
    if guess == a:
        print("Поздравляю вы угадали!")
        break
    elif guess > a:
        print("Неверно. Число больше нужного.")
        Try -= 1
    elif guess < a:
        print("Неверно. Число меньше нужного.")
        Try -= 1
    if Try == 0:
        print("Игра окончена")
        print(a)
        break