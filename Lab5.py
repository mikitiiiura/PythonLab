#Завдання 1--------------------------------
def find_by_key(dictionary, key):
    return dictionary.get(key, "Ключ не знайдено")

arr_dictionar = {'Bob': 20, 'Alina': 25, 'Yura': 20, 'Vika': 32}

print("Завдання 1:")

key_to_find = 'Bob'  # Вибираємо ключ, який точно є в словнику
print(f"Результат виконання для користувача {key_to_find}: {find_by_key(arr_dictionar, key_to_find)}")

#Завдання 2-------------------------------
import math


def approximate_function(x, epsilon):
    """Обчислює наближене значення функції e^(2x) за допомогою розкладу в ряд Тейлора."""
    term = 1  # Перший член ряду (2x)^0 / 0! = 1
    sum_approx = term
    n = 1

    while abs(term) > epsilon:
        term *= (2 * x) / n  # Наступний член ряду: (2x)^n / n!
        sum_approx += term
        n += 1

    return sum_approx, n


def compute_values(a, b, epsilon, m=10):
    """Обчислює значення функції на рівномірній сітці з m точками."""
    results = []
    step = (b - a) / (m - 1)

    for i in range(m):
        x = a + i * step
        exact_value = math.exp(2 * x)  # Точне значення e^(2x)
        approx_value, iterations = approximate_function(x, epsilon)
        accuracy = abs(exact_value - approx_value)
        results.append((x, exact_value, approx_value, accuracy, iterations))

    return results


def print_table(results):
    """Виводить результати у вигляді таблиці."""
    print(f"{'x':^10} | {'f(x) точне':^15} | {'f_набл(x)':^15} | {'ε Точність':^15} | {'К-сть ітерацій':^15}")
    print("-" * 72)

    for x, exact, approx, accuracy, iterations in results:
        print(f"{x:^10.5f} | {exact:^15.10f} | {approx:^15.10f} | {accuracy:^15.10f} | {iterations:^15}")

print("\nЗавдання 2:")
a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
epsilon = float(input("Введіть точність ε: "))

results = compute_values(a, b, epsilon)
print_table(results)

