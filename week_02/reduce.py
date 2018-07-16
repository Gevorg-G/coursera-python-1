from functools import reduce


def multiply(a, b):
    return a * b


# reduce бежит по списку слева направо (от 1 до 4 и перемножает последовательно числа)
# 1 * 2 = 2 -> 2 * 3 = 6 -> 6 * 4 = 24
# reduce позволяет сжимать данные, последовательно бегая по списку
print(reduce(multiply, range(1, 5)))

# reduce можно использовать вместе с lambda
print(reduce(lambda x, y: x * y, range(1, 5)))
