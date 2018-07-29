"""
Интерфейс для работы с файлами
"""

import os
import tempfile
import random


class File():
    def __init__(self, path):
        self.path = path
        self.current_position = 0

        if not os.path.exists(self.path):
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            open(self.path, 'a').close()

    def __add__(self, obj):
        sum_file_path = os.path.join(tempfile.gettempdir(), os.path.basename(os.path.splitext(self.path)[0])
                                     + "_" + os.path.basename(os.path.splitext(obj.path)[0]) + "_" + str(random.randrange(0, 1000)) + ".txt")

        with open(self.path) as first_file:
            first = first_file.read()

        with open(obj.path) as second_file:
            second = second_file.read()

        with open(sum_file_path, "a+") as f:
            f.write(first)
            f.write(second)

        return File(sum_file_path)

    def __iter__(self):
        with open(self.path) as f:
            for string in f:
                yield string

    def __str__(self):
        return self.path

    def write(self, text):
        with open(self.path, "a+") as f:
            f.write(text)

    def read(self):
        with open(self.path) as f:
            print(f.read())


# f1 = File("tmp/1.txt")

# for i in f1:
#     print(i)
