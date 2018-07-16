# https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D0%B4%D1%80%D0%B0%D1%82%D0%BD%D0%BE%D0%B5_%D1%83%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5
# Используется для того, чтобы прочитать аргумент (строку с числом), введённую в терминале
import sys
# Из этой библиотеки нам нужна функция sqrt, с помощью которой мы вычислим квадратный корень
import math


def quadratic_equation():
    # Считываем строку с коэффициентами
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    # Вычисляем детерминант
    if a == 0:
        print("Решений нет")
    elif (b ** 2 - 4 * a * c) < 0:
        print("Решений нет")
    elif (b ** 2 - 4 * a * c) == 0:
        print((-1 * b) / (2 * a))
        print((-1 * b) / (2 * a))
    else:
        print(int((-1 * b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a))
        print(int((-1 * b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a))


if __name__ == "__main__":
    quadratic_equation()
