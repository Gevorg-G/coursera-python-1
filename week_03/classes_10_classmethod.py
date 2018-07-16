"""
classmethod
"""

# Объяснение на английском: https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
# Объяснение на русском: http://qaru.site/questions/10955/meaning-of-classmethod-and-staticmethod-for-beginner
# Мы реализовали синтаксический анализ строки даты в одном месте и теперь можно повторно использовать.
#
# Инкапсуляция отлично работает здесь (если вы считаете, что вы можете реализовать синтаксический анализ строк
# как одну функцию в другом месте, это решение лучше подходит для парадокса ООП).
# cls - это объект, который содержит класс, а не экземпляр класса.
# Это довольно круто, потому что, если мы наследуем наш класс Date, все дети будут иметь также from_string.


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @classmethod
    def from_string(cls, full_name):
        name = full_name[0]
        surname = full_name[1]
        return cls(name, surname)


# В данном конкретном примере по сути, используя classmethod from_string,
# мы создаём экземпляр класса, но перед этим перерабатываем продящие данные
john_smith = Human.from_string(["John", "Smith"])

print(john_smith.name)
print(john_smith.surname)


# При этом мы точно также можем создать экземпляр класса обычным способом
kate_adams = Human("Kate", "Adams")

print(kate_adams.name)
print(kate_adams.surname)
