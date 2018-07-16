# Сделано по туториалу: https://www.youtube.com/watch?v=q94B9n_2nf0
#
# Простейший пример работы модуля argparse, который в данном случае считает число Фибоначчи для выбранного числа
# При наличии опционального аргумента записывает данные в файл
# При этом -q и -v взаимоисключающие аргументы
import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return a


def Main():
    # Добавляем парсер
    parser = argparse.ArgumentParser()
    # Добавляем группу взаимоисключающих параметров
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    # Добавляем описание аргумента
    # num — название аргумента, по нему будем обращаться
    # help — описание аргумента
    # type – тип
    parser.add_argument(
        "num", help="The fibonacci number you wish to calculate.", type=int)

    # Описываем опциональный аргумент
    # -o, --output — названия аргументов
    # help — описание
    # action="store_true" — показывает что мы просто храним запись о наличии / отсутствии аргумента
    parser.add_argument(
        "-o", "--output", help="Output result to a file.", action="store_true")
    # Считываем аргументы
    args = parser.parse_args()

    # Передаём в функцию аругмент num
    result = fib(args.num)

    # Выводим результат
    if args.verbose:
        print("Verbose: " + str(args.num) + " / " + str(result))
    elif args.quiet:
        print("Quiet: " + str(args.num) + " / " + str(result))
    else:
        print("Nor verbose or quiet: " + str(args.num) + " / " + str(result))

    # Записываем в файл при наличии аргумента
    if args.output:
        with open("fibonacci.txt", 'a') as f:
            f.write(str(result) + '\n')


if __name__ == '__main__':
    Main()

# Результаты вывода
# (week_02) MacBook-Pro-glechyan:week_02 glechan$ python3 argparse_03.py 11 -v
# Verbose: 11 / 89
# (week_02) MacBook-Pro-glechyan:week_02 glechan$ python3 argparse_03.py 11 --verbose
# Verbose: 11 / 89
# (week_02) MacBook-Pro-glechyan:week_02 glechan$ python3 argparse_03.py 11 -q
# Quiet: 11 / 89
# (week_02) MacBook-Pro-glechyan:week_02 glechan$ python3 argparse_03.py 11 --quiet
# Quiet: 11 / 89
# (week_02) MacBook-Pro-glechyan:week_02 glechan$ python3 argparse_03.py 11
# Nor verbose or quiet: 11 / 89
# (week_02) MacBook-Pro-glechyan:week_02 glechan$ python3 argparse_03.py 11 -q -v
# usage: argparse_03.py [-h] [-v | -q] [-o] num
# argparse_03.py: error: argument -v/--verbose: not allowed with argument -q/--quiet
# (week_02) MacBook-Pro-glechyan:week_02 glechan$
