numers = []
num = 1
second = []
third = []
fourth = []
fifth = []
sixth = []
seventh = []
eight = []
ninth = []
while True:
    num = num + 1
    numers.append(num)
    if num == 99:
        break
i = 0
while i < len(numers):
    if numers[i]%2 == 0:
        second.append(numers[i])
    i += 1
print(f'Крвтные 2:{second}')
i = 0
while i < len(numers):
    if numers[i]%3 == 0:
        third.append(numers[i])
    i += 1
print(f'Крвтные 3:{third}')
i = 0
while i < len(numers):
    if numers[i]%4 == 0:
        fourth.append(numers[i])
    i += 1
print(f'Крвтные 4:{fourth}')
i = 0
while i < len(numers):
    if numers[i]%5 == 0:
        fifth.append(numers[i])
    i += 1
print(f'Крвтные 5:{fifth}')
i = 0
while i < len(numers):
    if numers[i]%6 == 0:
        sixth.append(numers[i])
    i += 1
print(f'Крвтные 6:{sixth}')
i = 0
while i < len(numers):
    if numers[i]%7 == 0:
        seventh.append(numers[i])
    i += 1
print(f'Крвтные 7:{seventh}')
i = 0
while i < len(numers):
    if numers[i]%8 == 0:
        eight.append(numers[i])
    i += 1
print(f'Крвтные 8:{eight}')
i = 0
while i < len(numers):
    if numers[i]%9 == 0:
        ninth.append(numers[i])
    i += 1
print(f'Крвтные 9:{ninth}')