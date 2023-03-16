# -------------- Previously
name = 'Severus'
age = 30
num = [1, 2, 3, 4, 5, 6]

typ_name = type(name)
typ_age = type(age)
typ_num = type(num)
print(typ_age)


# -------------- Classes
class Planet:
    def __init__(self):
        self.name = 'Hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'Hoth System'

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


hoth = Planet()
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'Gravity is: {hoth.gravity}')
print(f'System is: {hoth.system}')
print(hoth.orbit())

# OK
