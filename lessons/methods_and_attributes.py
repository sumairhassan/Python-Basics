from space.planet import Planet
from space.calc import planet_mass, planet_vol

naboo = Planet('Naboo', 300000, 8, 'Naboo System')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f'{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}')









"""
old code before modules and packages

class Planet:

    shape = 'round' # class level attribute, for example same for all instances

    def __init__(self, name, radius, gravity, system): # these are instance attributes, unique to instance
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self): # these are instance methods, unique to instance
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod # class level method, common for planet
    def commons(cls):
        return f'All planet are {cls.shape} because of gravity'

# static method is a method which does not have access to self and class itself
# it only has access to the parameteres that we pass into it individually.
# dont take anything except the parameters that we pass.

    @staticmethod
    def spin(speed = "2000 miles per hour"):
        return f'The planet spins and spins a {speed}'   

#naboo = Planet('Naboo', 300000, 8, 'Naboo System')

#print(Planet.shape)
#print(naboo.shape)
#print(Planet.commons())
#print(naboo.commons())

#print(Planet.spin('a very high speed'))
# print(naboo.spin('a very high speed'))





# self has access to individual instance
# cls has access to class level attributes"""

