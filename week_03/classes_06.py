"""
Classes #6
"""


class Planet:
    """Класс для создания планет"""
    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1

    def __str__(self):
        return self.name


earth = Planet("Earth")
mars = Planet("Mars")

# Выведет 2
# Каждый раз при создании экземпляра класса
# счётчик количества экземпляров будет инкреминтироваться
print(Planet.count)
