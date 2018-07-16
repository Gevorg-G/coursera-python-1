class Planet:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


earth = Planet("Earth")
# Переопределённый __init__
print(earth.name)
# Переопределённый __str__
print(earth)
