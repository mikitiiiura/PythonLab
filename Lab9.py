import os
import datetime

# Завдання 1: Робота з файлами студентів
def task_1():
    print("\n=== Завдання 1: Робота з файлами студентів ===")

    # 1. Створення файлу з іменами студентів та їх середніми балами
    # print("\n1. Створення файлу з іменами студентів та їх середніми балами...")
    # def create_student_file(filename):
    #     students = [
    #         ("Іван Іванов", 85.5),
    #         ("Петро Петров", 92.0),
    #         ("Марія Сидорова", 78.3),
    #         ("Олена Коваленко", 88.7)
    #     ]
    #     with open(filename, 'w') as file:
    #         for name, score in students:
    #             file.write(f"{name}: {score}\n")
    #     print(f"Файл {filename} створено.")

    # create_student_file(os.path.join('data', 'students.txt'))

    # 2. Читання файлу
    print("\n2. Читання файлу...")
    def read_student_file(filename):
        with open(filename, 'r') as file:
            print(f"Вміст файлу {filename}:")
            for line in file:
                print(line, end='')

    read_student_file(os.path.join('data', 'students.txt'))

    # 3. Додавання нового студента
    print("\n3. Додавання нового студента...")
    def add_student(filename, name, score):
        with open(filename, 'a') as file:
            file.write(f"{name}: {score}\n")
        print(f"Студента {name} додано до файлу {filename}.")

    add_student(os.path.join('data', 'students.txt'), "Андрій Григоренко", 91.2)

    # 4. Пошук студента за ім'ям
    print("\n4. Пошук студента за ім'ям...")
    def find_student(filename, name):
        with open(filename, 'r') as file:
            print(f"Результат пошуку студента {name}:")
            for line in file:
                if name in line:
                    print(line, end='')

    find_student(os.path.join('data', 'students.txt'), "Марія Сидорова")

    # 5. Сортування студентів за середнім балом
    print("\n5. Сортування студентів за середнім балом...")
    def sort_students_by_score(filename):
        students = []
        with open(filename, 'r') as file:
            for line in file:
                name, score = line.strip().split(': ')
                students.append((name, float(score)))
        
        students.sort(key=lambda x: x[1], reverse=True)
        
        with open(filename, 'w') as file:
            for name, score in students:
                file.write(f"{name}: {score}\n")
        print(f"Файл {filename} відсортовано за середнім балом.")

    sort_students_by_score(os.path.join('data', 'students.txt'))

    # Перевірка відсортованого файлу
    print("\nПеревірка відсортованого файлу:")
    read_student_file(os.path.join('data', 'students.txt'))

# Завдання 2: Пошук рядка, який починається з літери «Т»
def task_2():
    print("\n=== Завдання 2: Пошук рядка, який починається з літери «Т» ===")

    

#     # Створення тестового файлу для завдання 2
#     print("\nСтворення тестового файлу для завдання 2...")
#     def create_test_file(filename):
#         text = '''Це тестовий файл.
# Тут є рядок, який починається з літери Т.
# А це інший рядок.'''
#         with open(filename, 'w') as file:
#             file.write(text)
#         print(f"Файл {filename} створено.")

#     create_test_file(os.path.join('data', 'test_file.txt'))

    # Пошук рядка, який починається з літери «Т»
    print("\nПошук рядка, який починається з літери «Т»...")
    def find_line_starting_with_T(filename):
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                if line.strip().startswith('Т'):
                    return i + 1  # Повертаємо номер рядка (починаючи з 1)
        return -1  # Якщо рядок не знайдено

    line_number = find_line_starting_with_T(os.path.join('data', 'test_file.txt'))
    if line_number != -1:
        print(f"Перший рядок, який починається з 'Т', знаходиться у рядку {line_number}.")
    else:
        print("Рядок, який починається з 'Т', не знайдено.")

# Головна програма
if __name__ == '__main__':
    # Перевірка наявності директорії data
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Створено директорію 'data'.")

    # Виконання завдання 1
    task_1()

    # Виконання завдання 2
    task_2()