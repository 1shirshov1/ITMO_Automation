class Page:  # создаем класс
    def __init__(self, url):      # конструктор класса def __init__ метод инициализации,  text, link - это еще аргументы
        self.url = url

    def get(self):
        print(self.url)

home = Page('https//:')
home.get()  # вызываем метод get

