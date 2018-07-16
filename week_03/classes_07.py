class Human:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __del__(self):
        print("Goodbye!")


human = Human()
# В данном случае деструктор отработает -
# но все же лучше создать метод и вызывать его явно
# Переопределение метода __del__ — это плохая практика, так лучше не делать
print(human)
