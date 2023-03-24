class Planety:
    # Class attribute
    shape = 'carret'

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
