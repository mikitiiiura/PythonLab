import math

def frange(start, stop, step):
    while start <= stop:
        yield round(start, 1)  #Округлюємо
        start += step

def calculate_y(x):
    try:
        return (5 * math.log10(x + 7)) / ((x + 3) ** 2)
    except ValueError as e:
        print(f"Помилка у значенні логарифма для x={x}: {e}") 
        return None
    except ZeroDivisionError as e:
        print(f"Помилка ділення на нуль для x={x}: {e}")
        return None

x_values = list(frange(1.2, 6.3, 0.4))  #Генеруємо список x

print(" x     |     y")
print("-----------------")
for x in x_values:
    y = calculate_y(x)
    if y is not None:
        print(f"{x:.1f}  |  {y:.5f}")
