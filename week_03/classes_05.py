class Planet:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Planet {self.name}"


mars = Planet("Mars")
print(mars)

# Добавит новый атрибут экземпляру класса
mars.name = "Second Earth?"
print(mars.name)

# Удаление атрибута класса. После этого к нему нельзя будет обратиться
# del mars.name
