side1 = int(input("Сторона 1: "))
side2 = int(input("Сторона 2: "))
side3 = int(input("Сторона 3: "))
if side1 + side2 >= side3 and side1 + side3 >= side2 and side2 + side3 >= side1:
    print("Данный треугольник может сушествовать")
    if side1 == side2 == side3:
        print("Также данный треугольник равносторонний")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Также данный треугольник являеться равнобедренным")
    else:
        print("Также данный треугольник являеться разностаронним")
else:
    print("К сожалению данный треугольник не может сушествовать")