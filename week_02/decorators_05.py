import dis
# #  Цепочки декораторов
# def bold(func):
#     def wrapped():
#         print("bold")
#         return "<b>" + func() + "<b>"
#     return wrapped


# def italic(func):
#     def wrapped():
#         print("italic")
#         return "<i>" + func() + "<i>"
#     return wrapped


# @bold
# @italic
# def text():
#     return "text"


# # 1. italic оборачивает text
# # 2. bold оборачивает italic
# # Таким образом получаем сначала <b> + italic + <b>
# print(text())


def mult(func):
    return lambda x: func(x * x)


def add(func):
    return lambda x: func(x + 4)


@mult
@add
def f1(x):
    return x


@add
@mult
def f2(x):
    return x


# Выведет 8: (2 * 2) + 4
print("Функция 1:", f1(2))
# Выведет 49: (3 + 4) * 7
print("Функция 2:", f2(3))

print("Байт-код f1 ______")
print(dis.dis(f1))
print("Байт-код f2 ______")
print(dis.dis(f2))
