# Пример из decorators_03.py, но с возможностью записывать в произвольный файл
# Для сложности я попробовал считывать имя файла из внешнего источника
import functools
import sys

# Получаем sys.argv[1]
log_file = sys.argv[1] + '.txt'


def logger(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))

            return result
        return wrapper
    return decorator


@logger(log_file)
def summator(num_list):
    return sum(num_list)


print("Тип сумматора: ", summator.__name__)
print("Результат в терминале:", summator(range(1, 6)))

with open(log_file, 'r') as f:
    print("Результат в файле", log_file, ":", f.read())
