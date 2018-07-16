def get_multiplier():
    # def inner_1(a, b):
    #     return a * b

    # def inner_2(a, b, c):
    #     return a * b * c

    def inner_3(a, b, c):
        return (a + b + c)

    return inner_3


multiplier = get_multiplier()

# Что выдавать в качестве результата определяется на основе того, что я хочу вернуть.
# То есть, если я хочу вернуть inner_3 (return inner_3), то я должен передать в multiplier 3 параметра, иначе будет ошибка.
# Соответственно, для inner_1 — это будет 2 параметра, иначе будет ошибка.
print("result:", multiplier(10, 11, 20))

# Тип multiplier поменялся на inner_3, потому что это тот результат, который я возвращаю
print("type:", multiplier.__name__)


def get_multiplier_2(number):
    def inner(a):
        return a * number
    return inner


# Замыкание — это когда во внутренней функции, используется переменная из уровня выше (get_multiplier_2)
multiplier_by_2 = get_multiplier_2(2)
print("result:", multiplier_by_2(10))
print("type:", multiplier_by_2.__name__)
