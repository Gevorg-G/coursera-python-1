"""
Classes #8
"""


class Planet:
    """This class describes planets"""
    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1

    def __str__(self):
        return self.name


earth = Planet("Earth")
mars = Planet("Mars")

print(earth.__dict__)
# Вывод: {'name': 'Earth', 'population': []}

earth.mass = 5.97e24
print(earth.__dict__)
# Вывод: {'name': 'Earth', 'population': [], 'mass': 5.97e+24}

print(Planet.__doc__)
# Вывод: This class describes planets
print(earth.__doc__)
# Вывод: This class describes planets

print(dir(earth))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# '__weakref__', 'count', 'mass', 'name', 'population']

print(earth.__class__)
# <class '__main__.Planet'>
