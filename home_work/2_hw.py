# def task1(a, b, c, d, e):
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


# c = 1+2j
# print(c, "комплексное число?",isinstance(c,complex))