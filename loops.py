# ------------------------- For Loops
mens = ['ruy', 'gael', 'bron', 'patrick']

# for man in mens:
#     print(man)

# Slice Method
# for man in mens[0:3]:
#     print(man)

# Using f-string methods
for man in mens:
    if man == 'bron':
        print(f'{man} - black belt')
        break
    else:
        print(man)


# ------------------------- While loops
age = 25
num = 0

# while num < age:
#     print(num)
#     num += 1

while num < age:
    if num == 0:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num += 1
