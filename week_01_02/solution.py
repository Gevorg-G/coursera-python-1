# Используется для того, чтобы прочитать аргумент (строку с числом), введённую в терминале
import sys


def steps():
    # Считываем строку с числом ступенек
    steps_num = int(sys.argv[1])
    # Итерируем
    for i in range(steps_num):
        print(" "*(steps_num-i-1)+"#"*(i+1))


if __name__ == "__main__":
    steps()
