"""
Первое задание у нас для разогрева.
Ваша задача написать Python-модуль solution.py, внутри которого определен
класс FileReader.
Инициализатор этого класса принимает аргумент - путь до файла на диске.

У класса должен быть метод read, возвращающий содержимое файла в виде строки.

Еще один момент - внутри метода read вы должны обрабатывать
исключение IOError, возникающее, когда файла, с которым был инициализирован
класс, на самом деле нет на жестком диске.

В случае возникновения такой ошибки метод read должен возвращать
пустую строку "".

То есть класс должен работать следующим образом:
reader = FileReader("example.txt")
print(reader.read())
"""

import os


class FileReader:
    """В этом классе мы будем читать и выводить файл"""

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """Возвращает содержимое файла в виде строки"""
        try:
            with open(self.filename, "r") as f:
                return f.read()
        except IOError:
            return ""


reader = FileReader("example.txt")
reader.read()
