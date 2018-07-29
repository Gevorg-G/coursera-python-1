# Создание процесса, модуль multiprocessing

from multiprocessing import Process


def f(name):
    print("hello", name)


p = Process(target=f, args=("Bob",))
# Создаст дочерний процесс
p.start()
# Завершит дочерний процесс
p.join()
