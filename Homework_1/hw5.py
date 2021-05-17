ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
let1 = int(ABC.index(input("Первая буква: "))) + 1
let2 = int(ABC.index(input("Вторая буква: "))) + 1
print(f'Позиция первой буквы {let1}')
print(f'Позиция второй буквы {let2}')
if let2 > let1:
    dis = let2 - (let1 + 1)
else:
    dis = (let1 - 1) - let2
print(f"Количесвто букв между ними {dis}")