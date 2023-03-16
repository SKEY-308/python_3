# ------------ Sorted() preserve the order
num = [1, 9, 6, 9, 7, 6, 8, 7, 6, 8, 6, 7, 6, 7, 8, 9, 7]

sort_num = sorted(num)
print(sort_num)

color = ['yellow', 'red', 'green', 'blue',
         'purple', 'brown', 'orange', 'yellow']

sort_color = sorted(color)
print(sort_color)

# ------------ Set() do not preserve the order
set_num = set(num)
print(set_num)

set_col = set(color)
print(set_col)


# ----------------------------------------------------------------
ninjas = {'ruy': 'black', 'yoshi': 'white', 'crystal': 'black'}
val = ninjas.values()
print(val)

set_val = set(ninjas.values())
print(set_val)


# ------------------- Exples of set and/or sort in functions --------------------------------
def belts_count(dictionary):
    belts = list(dictionary.values())
    for belt in belts:
        num = belts.count(belt)
        print(f"There are {num} {belt} belts")


severus_belts = {}

while True:
    name = input("Enter the name: ")
    belt = input("Enter the belt: ")
    severus_belts[name] = belt

    another = input("Add another ? (y/n)")
    if another == 'y':
        continue
    else:
        break

belts_count(severus_belts)
