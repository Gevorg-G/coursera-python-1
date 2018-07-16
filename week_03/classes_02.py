class Planet:
    pass


# Создаём экземпляр класса
planet = Planet()
print(planet)


# Создаём список планет
solar_system = []
for i in range(8):
    planet = Planet()
    solar_system.append(planet)

print(solar_system)

# Экземпляры класса хэшируются
solar_system_dict = {}
for i in range(8):
    planet = Planet()
    solar_system_dict[planet] = True

print(solar_system_dict)
