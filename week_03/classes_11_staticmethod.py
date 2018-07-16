"""
staticmethod
"""

# Объяснение на английском: https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
# Объяснение на русском: http://qaru.site/questions/10955/meaning-of-classmethod-and-staticmethod-for-beginner
# Мы реализовали синтаксический анализ строки даты в одном месте и теперь можно повторно использовать.
#
# Немного другой способ подумать об этом, который может быть полезен для кого-то...
# Метод класса используется в суперклассе, чтобы определить, как должен вести себя этот метод при его вызове с помощью разных дочерних классов. Статический метод используется, когда мы хотим вернуть одно и то же, независимо от дочернего класса, который мы вызываем.


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @staticmethod
    def from_string(full_name):
        name = full_name[0]
        surname = "Doe"
        return Human(name, surname)


# Работает похожим образом на classstring, но не получает на входе ссылку на класс или экземпляр класса
# По факту — это просто функция внутри класса
john_smith = Human.from_string(["John", "Smith"])

print(john_smith.name)
print(john_smith.surname)

print(john_smith.from_string(["Sam", "Lue"]).name)
print(john_smith.from_string(["Sam", "Lue"]).surname)


# При этом мы точно также можем создать экземпляр класса обычным способом
kate_adams = Human("Kate", "Adams")

print(kate_adams.name)
print(kate_adams.surname)
