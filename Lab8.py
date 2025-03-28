# Створити базовий клас "Комп’ютер". На його основі реалізувати класи "Ноутбук", 
# "Персональний комп’ютер" та "Сервер". Класи повинні мати можливість задавати та 
# отримувати параметри (вартість, модель, рік випуску тощо) задати за допомогою полів. 
# Для ноутбука повинна бути визначена діагональ екрана, для ПК та сервера – наявність 
# оптичного приводу, для сервера – тип (шафовий, підлоговий).

class Computer:
    def __init__(self, model, year, price):
        self._model = model
        self._year = year
        self._price = price

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def display_info(self):
        print(f"\nModel: {self._model}, Year: {self._year}, Price: {self._price}", end="")


class Laptop(Computer):
    def __init__(self, model, year, price, screen_size):
        super().__init__(model, year, price)
        self._screen_size = screen_size

    def get_screen_size(self):
        return self._screen_size

    def set_screen_size(self, screen_size):
        self._screen_size = screen_size

    def display_info(self):
        super().display_info()
        print(f" Screen Size: {self._screen_size} inches", end=" ")


class DesktopPC(Computer):
    def __init__(self, model, year, price, has_optical_drive):
        super().__init__(model, year, price)
        self._has_optical_drive = has_optical_drive

    def get_has_optical_drive(self):
        return self._has_optical_drive

    def set_has_optical_drive(self, has_optical_drive):
        self._has_optical_drive = has_optical_drive

    def display_info(self):
        super().display_info()
        print(f" Has Optical Drive: {'Yes' if self._has_optical_drive else 'No'}", end=" ")


class Server(Computer):
    def __init__(self, model, year, price, has_optical_drive, server_type):
        super().__init__(model, year, price)
        self._has_optical_drive = has_optical_drive
        self._server_type = server_type

    def get_has_optical_drive(self):
        return self._has_optical_drive

    def set_has_optical_drive(self, has_optical_drive):
        self._has_optical_drive = has_optical_drive

    def get_server_type(self):
        return self._server_type

    def set_server_type(self, server_type):
        self._server_type = server_type

    def display_info(self):
        super().display_info()
        print(f"Has Optical Drive: {'Yes' if self._has_optical_drive else 'No'}", end=" ")
        print(f"Server Type: {self._server_type}", end=" ")


# Приклад використання
laptop = Laptop("Dell XPS 13", 2021, 1200, 13.4)
desktop = DesktopPC("HP Pavilion", 2020, 800, True)
server = Server("Dell PowerEdge", 2019, 2500, False, "Rack-mounted")

laptop.display_info()
print()
desktop.display_info()
print()
server.display_info()

# Пошук за ознакою
computers = [laptop, desktop, server]

# Пошук комп'ютерів, випущених після 2020 року
print("\n\n\nComputers released after 2020:")
for computer in computers:
    if computer.get_year() > 2020:
        computer.display_info()
        print()