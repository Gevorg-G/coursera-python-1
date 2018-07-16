from functools import partial


def greeter(person, greeting):
    return '{}, {}!'.format(greeting, person)


# partial принимает на вход функцию и подменяет часть параметров каким-то значением
hier = partial(greeter, greeting="Hi")
helloer = partial(greeter, greeting="Hello")
# Можно поменить также все параметры вообще
hell = partial(greeter, person="John", greeting="Hey")

print(hier('brother'))
print(helloer('sir'))
print(hell())
