# lambda — это функции, которые нужны только локально и их не имеет смысла объявлять отдельно
print(list(map(lambda x: x ** 2, range(5))))
# Превращает range(5) из списка чисел в список строк
print(list(map(lambda x: str(x), range(5))))
# lambda также работает с filter
print(list(filter(lambda x: x % 2 == 0, range(10))))
