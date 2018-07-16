# Переопределение из classes_03.py, но для списков — метод __repr__
class Planet:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Planet {self.name}"


solar_system = []
planet_names = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]


for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)
