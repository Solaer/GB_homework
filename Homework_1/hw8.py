year = int(input("Введите год: "))
if year%4 == 0 and year%100 != 0 or year == 2000:
    print("Данный год являеться висакосным")
else:
    print("Данный год не являеться вискосным")