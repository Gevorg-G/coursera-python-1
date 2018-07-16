"""
Classes #8
"""


class Planet:
    """This class describes planets"""
    count = 0

    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        # Создание нового экземпляра класса
        # super() возвращает родителя текущего класса
        # obj — экземпляр класса
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        print("__init__ called")
        self.name = name

    def __str__(self):
        return self.name


earth = Planet("Earth")

# Порядок выполнения
# Сначала создаётся экземпляр
# __new__ called
# Потому он инициализируется
# __init__ called

# То есть при вызове Planet("Earth") произошло примерно следующее:
# planet = Planet.__new__(Planet, "Earth")
# if isinstance(planet, Planet):
#     Planet.__init__(planet, "Earth")
