# Списочные выражения позволяют быстро создавать списки. Работает чуть быстрее цикла
# number ** 2 — что хотим получить
# for number in range(10) — откуда хотим получить
square_list = [number ** 2 for number in range(10)]
print(square_list)

# Списочные выражения с условием
even_list = [num * 10 for num in range(11) if num % 2 == 0]
print(even_list)

# Можно создавать словари
square_map = {number: number ** 2 for number in range(5)}
print(square_map)

# Можно делать сеты
square_set = {number ** 2 for number in range(5)}
print(square_set)
