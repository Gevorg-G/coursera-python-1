# Используется для того, чтобы прочитать аргумент (строку с числом), введённую в терминале
import sys


def summary():
    # Считываем строку с числом
    digit_string = sys.argv[1]
    # Сюда будет складываться сумма
    sum = 0
    # Итерируем по строке
    for i in digit_string:
        sum += int(i)
    return sum


if __name__ == "__main__":
    print(summary())
