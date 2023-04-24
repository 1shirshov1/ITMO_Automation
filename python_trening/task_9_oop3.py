class Soda:  # создаем класс
    def __init__(self, ing = None):      # конструктор класса def __init__ метод инициализации,  text, link - это еще аргументы
        self.ing = ing

    def show_my_drink(self):
       if self.ing:
           print(f"добавка и {self.ing}")
       else:
           print("Обычная газировка")

drink1 = Soda()
drink2 = Soda('малина')
drink1.show_my_drink()
drink1.show_my_drink()