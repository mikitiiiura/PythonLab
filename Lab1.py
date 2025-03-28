import math

try:
    x = float(input("Введіть x: "))

    # Перевірка області визначення
    if x <= 0:
        raise ValueError("Логарифм lg(x) визначений тільки для x > 0.")
    if math.isclose(2, x):
        raise ValueError("Логарифм lg|2 - x| не визначений для x = 2.")
    
    # Обчислення чисельника
    numerator = math.sqrt(math.log10(abs(2 - x)) + math.log10(x))

    # Обчислення знаменника
    denominator = math.cbrt(math.tan(x)) + math.sqrt(math.cos(x) ** 3)

    if math.isclose(denominator, 0):
        raise ZeroDivisionError("Знаменник дорівнює нулю.")

    # Обчислення виразу
    c = math.sin(x) ** 2 - (numerator / denominator)

    print(f"Результат: {c}")

except ValueError as e:
    print(f"Помилка: {e}")
except ZeroDivisionError as e:
    print(f"Помилка: {e}")
except Exception as e:
    print(f"Непередбачена помилка: {e}")