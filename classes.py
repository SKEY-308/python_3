# -------------- Previously
name = 'Severus'
age = 30
num = [1, 2, 3, 4, 5, 6]

typ_name = type(name)
typ_age = type(age)
typ_num = type(num)
print(typ_num)


# -------------- Avec Class, nous avons attribuer des proprietés et method à la classe Planet
class Planet:
    # Attribute or Propriety
    def __init__(self):
        self.name = 'Hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'Hoth System'

    # Method
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


hoth = Planet()
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'Gravity is: {hoth.gravity}')
print(f'System is: {hoth.system}')
print(hoth.orbit())


planetY = Planet()
print(planetY.orbit())


# ------------------------------ The init function : class personnalisée

# ---------- Ici, nous avons créer une instance multiple de la class Planet
class Planet:
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
print(hoth.name)

naboo = Planet('Naboo', 300000, 8, 'Naboo System')
print(naboo.orbit())


# ------------------------------------ Methods & Attributes
class PlanetTwo:
    # Class attribute
    shape = 'round'

    # Instance attribute
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    # Instance Method
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    # Class Method
    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

     # Static Method
    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'The planet spins and spins at {speed}'


naboo = PlanetTwo('Naboo', 300000, 8, 'Naboo System')


print(PlanetTwo.shape)
print(naboo.shape)
# ---------
# print(Planet.name), inacessibl parcq cè une instance proprieté ou attribut de Planet
print(PlanetTwo.commons())
print(naboo.commons())
# print(PlanetTwo.orbit()), inacessibl parcq cè une instance method de Planet

# ------------
print(PlanetTwo.spin())
print(PlanetTwo.spin('a very high speed'))
# print(naboo.spin('a very high speed'))
