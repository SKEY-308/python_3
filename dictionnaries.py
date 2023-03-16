james_belts = {"crystal": "red", "ruy": "black"}

print(james_belts["crystal"])
print(james_belts["ruy"])

# dictionnaries
print('yoshi' in james_belts)
print('ruy' in james_belts)

print(james_belts.keys())

print(list(james_belts.keys()))

print(james_belts.values())
vals = list(james_belts.values())
print(vals)

# Si celle ci m'affich 1, cela veut dire que 'red' existe ds james_belts.values() et si c'est O cela voudrai dir n'exist pas
print(vals.count('red'))

print('Value pink, n\'existe pas et me retourn: ', vals.count('pinks'))

# Ajout d'elm
james_belts["aria"] = 'blue'
print(james_belts)


person = dict(name="John", age=25, height='5ft')
print(person)


# ----------------------------------- Exples
def intro(dictionary):
    for key, val in dictionary.items():
        print(f"I am {key} and I am {val} belts")


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

intro(severus_belts)
