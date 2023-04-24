class Button:  # создаем класс
    def __init__(self, text, link):      # конструктор класса def __init__ метод инициализации,  text, link - это еще аргументы
        self.text = text                # тут они уже атрибуты
        self.link = link                # тут они уже атрибуты

# Создаем экземпляры класса

home = Button('Домой', '/home')   # создаем объект home   по тому же типу def __init__(self, text, link):
catalog_msk = Button('каталог', "/msk/catalog")   # создаем второй объект

# Получаем доступ к атрибутам
print(home.text)
print('кнопка ' + home.text + " имеет ссылку " + home.link)

print("\n")
print(catalog_msk.text)
print('кнопка' + catalog_msk.text + " имеет ссылку " + catalog_msk.link)

#__________________

class ButtonTwo:
    def __init__(self, text, linc, loc):
        self.text = text
        self.linc = linc
        self.loc = loc


    def click(self):     #  добавляем метод click
        return "Клик по локатору - {}" .format(self.loc)     # фигурные скобки вставляют переменную   , обращаемся к локатору (self.loc)

# оздаем экземпляры класса
home_two = ButtonTwo('Домой', "/home", "button#home")  # home_two - это объект по классу ButtonTwo - button#home  # локатор,

# Вызываем метод
print (home_two.click())