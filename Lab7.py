# Розробити клас "домашня бібліотека". Додати
# конструктор, який приймає ціле число – порядковий номер
# книги та словник, що містить інформацію про книгу наступному
# форматі: 1) автор; 2) назва; 3) видавництво; 4) жанр; 5) рік
# видання.
# Реалізувати можливість роботи з довільним числом книг,
# пошуку по книгах за декількома параметрами (за автором, за
# роком видання, за жанром тощо), додавання книг у бібліотеку,
# видалення книг з неї, доступу до книги за номером. Написати
# програму, що буде демонструвати всі розроблені елементи
# класу.

class HomeLibrary:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, book_info):
        if book_id in self.books:
            print(f"Книга з номером {book_id} вже існує.")
        else:
            self.books[book_id] = book_info
            print(f"Книга з номером {book_id} додана до бібліотеки.")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Книга з номером {book_id} видалена з бібліотеки.")
        else:
            print(f"Книга з номером {book_id} не знайдена.")

    def find_by_author(self, author):
        found_books = {book_id: info for book_id, info in self.books.items() if info['автор'] == author}
        return found_books

    def find_by_year(self, year):
        found_books = {book_id: info for book_id, info in self.books.items() if info['рік видання'] == year}
        return found_books

    def find_by_genre(self, genre):
        found_books = {book_id: info for book_id, info in self.books.items() if info['жанр'] == genre}
        return found_books

    def get_book_by_id(self, book_id):
        return self.books.get(book_id, "Книга з таким номером не знайдена.")

    def display_all_books(self):
        for book_id, info in self.books.items():
            print(f"Номер книги: {book_id}")
            for key, value in info.items():
                print(f"{key}: {value}")
            print("-" * 20)

# Демонстрація роботи класу
library = HomeLibrary()

# Додавання книг
library.add_book(1, {
    'автор': 'Джордж Орвелл',
    'назва': '1984',
    'видавництво': 'Secker & Warburg',
    'жанр': 'Антиутопія',
    'рік видання': 1949
})

library.add_book(2, {
    'автор': 'Джордж Орвелл',
    'назва': 'Ферма тварин',
    'видавництво': 'Secker & Warburg',
    'жанр': 'Алегорія',
    'рік видання': 1945
})

library.add_book(3, {
    'автор': 'Джейн Остін',
    'назва': 'Гордість і упередження',
    'видавництво': 'T. Egerton, Whitehall',
    'жанр': 'Роман',
    'рік видання': 1813
})

# Виведення всіх книг
print("Всі книги в бібліотеці:")
library.display_all_books()

# Пошук книг за автором
print("Книги Джорджа Орвелла:")
found_books = library.find_by_author('Джордж Орвелл')
for book_id, info in found_books.items():
    print(f"Номер книги: {book_id}, Назва: {info['назва']}")

# Пошук книг за роком видання
print("Книги, видані у 1949 році:")
found_books = library.find_by_year(1949)
for book_id, info in found_books.items():
    print(f"Номер книги: {book_id}, Назва: {info['назва']}")

# Пошук книг за жанром
print("Книги жанру 'Роман':")
found_books = library.find_by_genre('Роман')
for book_id, info in found_books.items():
    print(f"Номер книги: {book_id}, Назва: {info['назва']}")

# Отримання книги за номером
print("Інформація про книгу з номером 2:")
print(library.get_book_by_id(2))

# Видалення книги
library.remove_book(2)
print("Всі книги після видалення:")
library.display_all_books()
