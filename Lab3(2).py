import random

# Функція для генерації матриці розміром m x n з випадковими числами від 0 до 20
def generate_matrix(m, n):
    return [[random.randint(0, 20) for _ in range(n)] for _ in range(m)]

# Функція для обчислення суми елементів рядків, де на побічній діагоналі є невід'ємні числа
def sum_rows_with_nonneg_on_secondary_diag(matrix):
    m, n = len(matrix), len(matrix[0])  # Отримуємо розміри матриці (кількість рядків і стовпців)
    total_sum = 0  # Змінна для зберігання загальної суми

    # Проходимо по елементах побічної діагоналі
    for i in range(min(m, n)):
        # Перевіряємо, чи елемент на побічній діагоналі невід'ємний
        if matrix[i][n - 1 - i] >= 0:
            # Якщо так, додаємо суму елементів цього рядка до загальної суми
            total_sum += sum(matrix[i])

    return total_sum  # Повертаємо загальну суму

# Отримуємо довжину прізвища та імені користувача
surname_length = len(input("Введіть ваше прізвище: "))
name_length = len(input("Введіть ваше ім'я: "))

# Генеруємо матрицю на основі довжини прізвища та імені
matrix = generate_matrix(surname_length, name_length)

# Виводимо згенеровану матрицю
print("Згенерована матриця:")
for row in matrix:
    print(row)

# Обчислюємо суму елементів рядків з невід'ємними числами на побічній діагоналі
result = sum_rows_with_nonneg_on_secondary_diag(matrix)

# Виводимо результат
print("Сума елементів рядків з невід’ємними числами на побічній діагоналі:", result)