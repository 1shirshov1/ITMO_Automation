# Задача 1 (* не понял указания создайте функцию task1(
# def task1(a, b, c, d, e):
print("Задача 1", '\n')
# def task_1(a, b, c, d, e):
a = 2
print(a, "относится к типу", type(a))

b = 15.0001
print(b, "относится к типу",type(b))

c = "строка"
print(c, "относится к типу",type(c))

d = [5, 10, 15, 29, 30, 40]
print(d, "относится к типу",type(d))

e = True
if e:
    print(e, 'e = True', type(e))
else:
    print("a != True")

# Задача 2  (* не понял указания создайте функцию task2(.
print("Задача 2" + '\n')
f = [1, 2, 3, 5, 8, 13, 21]
print("f[0:3]=", f[0:3])

# print(c, "комплексное число?",isinstance(c,complex))

# Задача 3
print("Задача 3" + '\n')

def task_3(g =2) -> int:
    return  g * g
print(task_3)