# Пример из decorators_02.py, но с произвольным количеством аргументов — *args, **kwargs
import functools


def logger(func):
    # Благодаря этой штуке тип сумматора остался summator
    # Это будет полезно при отладке программы
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))

        return result
    return wrapper


# После оборачивания через @logger summator становится logger(summator), то есть wrapper (см. возвращаемый результат)
# Таким образом в записи logger(func) func == summator
# То есть внутри wrapper выполнится:
# 1. Функция суматор
# 2. Потом всё это запишется в файл
@logger
def summator(num_list):
    return sum(num_list)


print("Тип сумматора: ", summator.__name__)
print("Результат в терминале:", summator(range(1, 6)))

with open('log.txt', 'r') as f:
    print("Результат в файле log.txt:", f.read())
