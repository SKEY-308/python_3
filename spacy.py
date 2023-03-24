from space.planet import Planety
from space.calc import planet_mass, planet_vol


nano = Planety('Nano', 5000000, 8.9, 'Nano system')

nanoMass = planet_mass(nano.gravity, nano.radius)

nanoVol = planet_vol(nano.radius)

print(f'Nano Masse is equal to : {nanoMass}')
print(f'Nano Volume is equal to : {nanoVol}')
print(f'{nano.name} has a mass of "{nanoMass}" and a volume of "{nanoVol}"')
