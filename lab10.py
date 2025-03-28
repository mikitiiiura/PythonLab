import pyodbc

class HomeLibrary:
    def __init__(self, connection_string=None):
        self.books = {}
        self.connection_string = connection_string
        if connection_string:
            self.create_table()

    def create_table(self):
        with pyodbc.connect(self.connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Books')
                BEGIN
                    CREATE TABLE Books (
                        BookId INT PRIMARY KEY,
                        Author NVARCHAR(100),
                        Title NVARCHAR(100),
                        Publisher NVARCHAR(100),
                        Genre NVARCHAR(50),
                        Year INT
                    )
                END
            """)
            conn.commit()

    def add_book(self, book_id, book_info):
        if book_id in self.books:
            print(f"Книга з номером {book_id} вже існує.")
        else:
            self.books[book_id] = book_info
            print(f"Книга з номером {book_id} додана до бібліотеки.")
            
            if self.connection_string:
                self._save_to_db(book_id, book_info)

    def _save_to_db(self, book_id, book_info):
        try:
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO Books (BookId, Author, Title, Publisher, Genre, Year)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, book_id, 
                   book_info['автор'], 
                   book_info['назва'], 
                   book_info['видавництво'], 
                   book_info['жанр'], 
                   book_info['рік видання'])
                conn.commit()
        except Exception as e:
            print(f"Помилка при збереженні в базу даних: {e}")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Книга з номером {book_id} видалена з бібліотеки.")
            
            if self.connection_string:
                self._delete_from_db(book_id)
        else:
            print(f"Книга з номером {book_id} не знайдена.")

    def _delete_from_db(self, book_id):
        try:
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Books WHERE BookId = ?", book_id)
                conn.commit()
        except Exception as e:
            print(f"Помилка при видаленні з бази даних: {e}")

    def find_by_author(self, author):
        found_books = {book_id: info for book_id, info in self.books.items() if info['автор'] == author}
        
        if self.connection_string:
            found_books.update(self._search_in_db('Author', author))
            
        return found_books

    def find_by_year(self, year):
        found_books = {book_id: info for book_id, info in self.books.items() if info['рік видання'] == year}
        
        if self.connection_string:
            found_books.update(self._search_in_db('Year', year))
            
        return found_books

    def find_by_genre(self, genre):
        found_books = {book_id: info for book_id, info in self.books.items() if info['жанр'] == genre}
        
        if self.connection_string:
            found_books.update(self._search_in_db('Genre', genre))
            
        return found_books

    def _search_in_db(self, field, value):
        try:
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM Books WHERE {field} = ?", value)
                rows = cursor.fetchall()
                
                return {
                    row.BookId: {
                        'автор': row.Author,
                        'назва': row.Title,
                        'видавництво': row.Publisher,
                        'жанр': row.Genre,
                        'рік видання': row.Year
                    } for row in rows
                }
        except Exception as e:
            print(f"Помилка при пошуку в базі даних: {e}")
            return {}

    def get_book_by_id(self, book_id):
        book = self.books.get(book_id)
        if book:
            return book
            
        if self.connection_string:
            return self._get_from_db_by_id(book_id)
            
        return "Книга з таким номером не знайдена."

    def _get_from_db_by_id(self, book_id):
        try:
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Books WHERE BookId = ?", book_id)
                row = cursor.fetchone()
                
                if row:
                    return {
                        'автор': row.Author,
                        'назва': row.Title,
                        'видавництво': row.Publisher,
                        'жанр': row.Genre,
                        'рік видання': row.Year
                    }
                else:
                    return "Книга з таким номером не знайдена."
        except Exception as e:
            print(f"Помилка при отриманні книги з бази даних: {e}")
            return "Помилка при отриманні книги з бази даних."

    def load_from_db(self):
        if not self.connection_string:
            return
            
        try:
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Books")
                rows = cursor.fetchall()
                
                for row in rows:
                    self.books[row.BookId] = {
                        'автор': row.Author,
                        'назва': row.Title,
                        'видавництво': row.Publisher,
                        'жанр': row.Genre,
                        'рік видання': row.Year
                    }
        except Exception as e:
            print(f"Помилка при завантаженні з бази даних: {e}")

    def display_all_books(self):
        if self.connection_string:
            self.load_from_db()
            
        for book_id, info in self.books.items():
            print(f"Номер книги: {book_id}")
            for key, value in info.items():
                print(f"{key}: {value}")
            print("-" * 20)


def show_menu():
    print("\nМеню домашньої бібліотеки:")
    print("1. Показати всі книги")
    print("2. Додати нову книгу")
    print("3. Видалити книгу")
    print("4. Пошук за автором")
    print("5. Пошук за роком видання")
    print("6. Пошук за жанром")
    print("7. Знайти книгу за номером")
    print("8. Вийти")

def add_book_ui(library):
    print("\nДодавання нової книги:")
    try:
        book_id = int(input("Введіть номер книги: "))
        author = input("Автор: ")
        title = input("Назва: ")
        publisher = input("Видавництво: ")
        genre = input("Жанр: ")
        year = int(input("Рік видання: "))
        
        book_info = {
            'автор': author,
            'назва': title,
            'видавництво': publisher,
            'жанр': genre,
            'рік видання': year
        }
        
        library.add_book(book_id, book_info)
    except ValueError:
        print("Помилка: номер книги та рік видання повинні бути числами")

def delete_book_ui(library):
    print("\nВидалення книги:")
    try:
        book_id = int(input("Введіть номер книги для видалення: "))
        library.remove_book(book_id)
    except ValueError:
        print("Помилка: номер книги повинен бути числом")

def search_by_author_ui(library):
    print("\nПошук за автором:")
    author = input("Введіть ім'я автора: ")
    found_books = library.find_by_author(author)
    if found_books:
        print("Знайдені книги:")
        for book_id, info in found_books.items():
            print(f"\nНомер книги: {book_id}")
            for key, value in info.items():
                print(f"{key}: {value}")
    else:
        print("Книги цього автора не знайдено")

def search_by_year_ui(library):
    print("\nПошук за роком видання:")
    try:
        year = int(input("Введіть рік видання: "))
        found_books = library.find_by_year(year)
        if found_books:
            print("Знайдені книги:")
            for book_id, info in found_books.items():
                print(f"\nНомер книги: {book_id}")
                for key, value in info.items():
                    print(f"{key}: {value}")
        else:
            print("Книги за цей рік не знайдено")
    except ValueError:
        print("Помилка: рік повинен бути числом")

def search_by_genre_ui(library):
    print("\nПошук за жанром:")
    genre = input("Введіть жанр: ")
    found_books = library.find_by_genre(genre)
    if found_books:
        print("Знайдені книги:")
        for book_id, info in found_books.items():
            print(f"\nНомер книги: {book_id}")
            for key, value in info.items():
                print(f"{key}: {value}")
    else:
        print("Книги цього жанру не знайдено")

def get_book_by_id_ui(library):
    print("\nПошук книги за номером:")
    try:
        book_id = int(input("Введіть номер книги: "))
        book = library.get_book_by_id(book_id)
        if isinstance(book, dict):
            print("\nІнформація про книгу:")
            for key, value in book.items():
                print(f"{key}: {value}")
        else:
            print(book)
    except ValueError:
        print("Помилка: номер книги повинен бути числом")

def main():
    # Підключення до бази даних
    connection_string = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-9KT5M4L\\SQLEXPRESS;"
        "Database=Lab10Python;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    
    # Створення об'єкту бібліотеки
    library = HomeLibrary(connection_string)
    
    # Головний цикл меню
    while True:
        show_menu()
        choice = input("\nВиберіть опцію (1-8): ")
        
        if choice == '1':
            print("\nВсі книги в бібліотеці:")
            library.display_all_books()
        elif choice == '2':
            add_book_ui(library)
        elif choice == '3':
            delete_book_ui(library)
        elif choice == '4':
            search_by_author_ui(library)
        elif choice == '5':
            search_by_year_ui(library)
        elif choice == '6':
            search_by_genre_ui(library)
        elif choice == '7':
            get_book_by_id_ui(library)
        elif choice == '8':
            print("Дякую за використання бібліотеки. До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, введіть число від 1 до 8.")
        
        input("\nНатисніть Enter для продовження...")

if __name__ == "__main__":
    main()



































# import pyodbc

# class HomeLibrary:
#     def __init__(self, connection_string=None):
#         self.books = {}
#         self.connection_string = connection_string
#         if connection_string:
#             self.create_table()

#     def create_table(self):
#         with pyodbc.connect(self.connection_string) as conn:
#             cursor = conn.cursor()
#             cursor.execute("""
#                 IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Books')
#                 BEGIN
#                     CREATE TABLE Books (
#                         BookId INT PRIMARY KEY,
#                         Author NVARCHAR(100),
#                         Title NVARCHAR(100),
#                         Publisher NVARCHAR(100),
#                         Genre NVARCHAR(50),
#                         Year INT
#                     )
#                 END
#             """)
#             conn.commit()

#     def add_book(self, book_id, book_info):
#         if book_id in self.books:
#             print(f"Книга з номером {book_id} вже існує.")
#         else:
#             self.books[book_id] = book_info
#             print(f"Книга з номером {book_id} додана до бібліотеки.")
            
#             if self.connection_string:
#                 self._save_to_db(book_id, book_info)

#     def _save_to_db(self, book_id, book_info):
#         try:
#             with pyodbc.connect(self.connection_string) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("""
#                     INSERT INTO Books (BookId, Author, Title, Publisher, Genre, Year)
#                     VALUES (?, ?, ?, ?, ?, ?)
#                 """, book_id, 
#                    book_info['автор'], 
#                    book_info['назва'], 
#                    book_info['видавництво'], 
#                    book_info['жанр'], 
#                    book_info['рік видання'])
#                 conn.commit()
#         except Exception as e:
#             print(f"Помилка при збереженні в базу даних: {e}")

#     def remove_book(self, book_id):
#         if book_id in self.books:
#             del self.books[book_id]
#             print(f"Книга з номером {book_id} видалена з бібліотеки.")
            
#             if self.connection_string:
#                 self._delete_from_db(book_id)
#         else:
#             print(f"Книга з номером {book_id} не знайдена.")

#     def _delete_from_db(self, book_id):
#         try:
#             with pyodbc.connect(self.connection_string) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("DELETE FROM Books WHERE BookId = ?", book_id)
#                 conn.commit()
#         except Exception as e:
#             print(f"Помилка при видаленні з бази даних: {e}")

#     def find_by_author(self, author):
#         found_books = {book_id: info for book_id, info in self.books.items() if info['автор'] == author}
        
#         if self.connection_string:
#             found_books.update(self._search_in_db('Author', author))
            
#         return found_books

#     def find_by_year(self, year):
#         found_books = {book_id: info for book_id, info in self.books.items() if info['рік видання'] == year}
        
#         if self.connection_string:
#             found_books.update(self._search_in_db('Year', year))
            
#         return found_books

#     def find_by_genre(self, genre):
#         found_books = {book_id: info for book_id, info in self.books.items() if info['жанр'] == genre}
        
#         if self.connection_string:
#             found_books.update(self._search_in_db('Genre', genre))
            
#         return found_books

#     def _search_in_db(self, field, value):
#         try:
#             with pyodbc.connect(self.connection_string) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute(f"SELECT * FROM Books WHERE {field} = ?", value)
#                 rows = cursor.fetchall()
                
#                 return {
#                     row.BookId: {
#                         'автор': row.Author,
#                         'назва': row.Title,
#                         'видавництво': row.Publisher,
#                         'жанр': row.Genre,
#                         'рік видання': row.Year
#                     } for row in rows
#                 }
#         except Exception as e:
#             print(f"Помилка при пошуку в базі даних: {e}")
#             return {}

#     def get_book_by_id(self, book_id):
#         book = self.books.get(book_id)
#         if book:
#             return book
            
#         if self.connection_string:
#             return self._get_from_db_by_id(book_id)
            
#         return "Книга з таким номером не знайдена."

#     def _get_from_db_by_id(self, book_id):
#         try:
#             with pyodbc.connect(self.connection_string) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("SELECT * FROM Books WHERE BookId = ?", book_id)
#                 row = cursor.fetchone()
                
#                 if row:
#                     return {
#                         'автор': row.Author,
#                         'назва': row.Title,
#                         'видавництво': row.Publisher,
#                         'жанр': row.Genre,
#                         'рік видання': row.Year
#                     }
#                 else:
#                     return "Книга з таким номером не знайдена."
#         except Exception as e:
#             print(f"Помилка при отриманні книги з бази даних: {e}")
#             return "Помилка при отриманні книги з бази даних."

#     def load_from_db(self):
#         if not self.connection_string:
#             return
            
#         try:
#             with pyodbc.connect(self.connection_string) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("SELECT * FROM Books")
#                 rows = cursor.fetchall()
                
#                 for row in rows:
#                     self.books[row.BookId] = {
#                         'автор': row.Author,
#                         'назва': row.Title,
#                         'видавництво': row.Publisher,
#                         'жанр': row.Genre,
#                         'рік видання': row.Year
#                     }
#         except Exception as e:
#             print(f"Помилка при завантаженні з бази даних: {e}")

#     def display_all_books(self):
#         if self.connection_string:
#             self.load_from_db()
            
#         for book_id, info in self.books.items():
#             print(f"Номер книги: {book_id}")
#             for key, value in info.items():
#                 print(f"{key}: {value}")
#             print("-" * 20)

# # Демонстрація роботи класу з підключенням до бази даних
# connection_string = (
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=DESKTOP-9KT5M4L\\SQLEXPRESS;"
#     "Database=Lab10Python;"
#     "Trusted_Connection=yes;"
#     "TrustServerCertificate=yes;"
# )

# #connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={"DESKTOP-9KT5M4L\\SQLEXPRESS"};DATABASE={"Lab10Python"};UID={"atmit"};PWD={"root"}'

# library = HomeLibrary(connection_string)

# # # Додавання книг
# # library.add_book(1, {
# #     'автор': 'Джордж Орвелл',
# #     'назва': '1984',
# #     'видавництво': 'Secker & Warburg',
# #     'жанр': 'Антиутопія',
# #     'рік видання': 1949
# # })

# # library.add_book(2, {
# #     'автор': 'Джордж Орвелл',
# #     'назва': 'Ферма тварин',
# #     'видавництво': 'Secker & Warburg',
# #     'жанр': 'Алегорія',
# #     'рік видання': 1945
# # })

# # library.add_book(3, {
# #     'автор': 'Джейн Остін',
# #     'назва': 'Гордість і упередження',
# #     'видавництво': 'T. Egerton, Whitehall',
# #     'жанр': 'Роман',
# #     'рік видання': 1813
# # })

# # Виведення всіх книг (тепер з бази даних)
# print("Всі книги в бібліотеці:")
# library.display_all_books()

# # Пошук книг за автором (тепер і в базі даних)
# print("Книги Джорджа Орвелла:")
# found_books = library.find_by_author('Джордж Орвелл')
# for book_id, info in found_books.items():
#     print(f"Номер книги: {book_id}, Назва: {info['назва']}")

# # Пошук книг за роком видання (тепер і в базі даних)
# print("Книги, видані у 1949 році:")
# found_books = library.find_by_year(1949)
# for book_id, info in found_books.items():
#     print(f"Номер книги: {book_id}, Назва: {info['назва']}")

# # Пошук книг за жанром (тепер і в базі даних)
# print("Книги жанру 'Роман':")
# found_books = library.find_by_genre('Роман')
# for book_id, info in found_books.items():
#     print(f"Номер книги: {book_id}, Назва: {info['назва']}")

# # Отримання книги за номером (тепер і з бази даних)
# print("Інформація про книгу з номером 2:")
# print(library.get_book_by_id(2))

# # # Видалення книги (тепер і з бази даних)
# # library.remove_book(2)
# # print("Всі книги після видалення:")
# # library.display_all_books()
