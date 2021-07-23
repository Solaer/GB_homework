num = input("Введите число: ")
mun = 0
mun = str(mun)
over = 0
i = 1
lenght = len(num) #Переменная на которой все держиться
while len(mun) < lenght:
    over = int(num)//(10**(lenght - i))
    num = int(num) - (over * (10**(lenght-i)))
    num = str(num)
    mun = over *(10**(i-1)) + int(mun)
    mun = str(mun)
    i += 1
print(mun)



#Писать такой код без использования массивов и списков это АД