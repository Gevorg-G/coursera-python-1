# Простейший пример работы модуля argparse, который в данном случае считает число Фибоначчи для выбранного числа
import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return a


def Main():
    # Добавляем парсер
    parser = argparse.ArgumentParser()
    # Добавляем описание аргумента
    # num — название аргумента, по нему будем обращаться
    # help — описание аргумента
    # type – тип
    parser.add_argument(
        "num", help="The fibonacci number you wish to calculate.", type=int)

    # Считываем аргументы
    args = parser.parse_args()

    # Передаём в функцию аругмент num
    result = fib(args.num)

    # Выводим результат
    print("The " + str(args.num) + "th fib number is " + str(result))


if __name__ == '__main__':
    Main()
