def squarify(a):
    return a ** 2


# map принимает на вход функцию и итерируемый объект
# Мы вокруг map оборачиваем в list, потому что map возвращает map-object, а list конвертирует его в список
# Аналог этого: https://s.mail.ru/DTWT/ni3QH4E4e
print(list(map(squarify, range(5))))
