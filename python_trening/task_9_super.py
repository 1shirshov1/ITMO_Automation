class A:
    def __init__(self):    # если после (self) будет аргумент то его надо указать в дочернем
        self.x = 10

...

class B(A):
    def __init__(self):
        super().__init__()   # вот тут в  init__() нужно было бы указаьб атрибут
        self.y = self.x + 5

print(B().y)
b = B()
print(b.y)
