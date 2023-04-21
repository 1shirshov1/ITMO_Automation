# пределяем функцию
def add(x, y):
    return x + y

# вызываем функцию
print(add(1, 2))

# вызываем функцию с другими аргументами
print(add("I a", 'm tester'))

def arg(a, b, c=2, d=3):
    return a + b + c + d

print(arg(1, 1, 1, 1))

print(arg(2, 2))

print(arg(2, 2, 4, 1))  # можно написать print(arg(2, 2, "3", 1))  и из-за  "3"
# будет ошибка потомучто он воспримет данное значение как текст т.е. другой тип дпнных.


def range_arg(a, b, c, d):
    return a + " " + b + " " + c + " " + d

print(range_arg('1', '2', '3', '4'))
print(range_arg('1', '2', d='3', c='4'))

def test(a=(1, 2, 3, 4)):  # Задача 1 _________________________________________
    return a[0]
print(test())

def test2(radius, pi=3.14):    # Задача 2 _____________________________________
    return pi * radius * radius
print(test2)


