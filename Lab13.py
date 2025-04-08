# Лабораторна робота №13
# Варіант 12
# Візуалізація математичних функцій з використанням matplotlib

import numpy as np
import matplotlib.pyplot as plt

# === Приклад 1 — Набір точок ===
plt.plot([1, 3, 2, 4])
plt.title('Приклад 1 — Набір точок')
plt.grid(True)
plt.savefig('example1.png', dpi=200)
plt.show()


# === Приклад 2 — Функція ===
def f(t):
    return t ** 2 * np.exp(-t ** 2)

t = np.linspace(0, 3, 51)
y = f(t)

plt.plot(t, y)
plt.title('Приклад 2 — Функція')
plt.grid(True)
plt.savefig('example2.png', dpi=200)
plt.show()


# === Приклад 3 — Налаштування вигляду графіків ===
t = np.linspace(0, 3, 51)
y = t ** 2 * np.exp(-t ** 2)

plt.plot(t, y, 'g--', label='t^2*exp(-t^2)')
plt.axis([0, 3, -0.05, 0.5])
plt.xlabel('t')
plt.ylabel('y')
plt.title('My first normal plot')
plt.legend()
plt.grid(True)
plt.savefig('example3.png', dpi=200)
plt.show()


# === Приклад 4 — Маркери, кілька графіків ===
t = np.linspace(0, 5, 100)
y1 = np.sin(t)
y2 = np.cos(t)
y3 = np.sin(t) * np.cos(t)

plt.plot(t, y1, 'b-o', label='sin(t)')
plt.plot(t, y2, 'r--s', label='cos(t)')
plt.plot(t, y3, 'g-.^', label='sin(t)*cos(t)')
plt.title('Приклад 4 — Кілька графіків')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('example4.png', dpi=200)
plt.show()


# === Приклад 5 — Встановлення міток осей ===
x = [5, 3, 7, 2, 4, 1]
plt.plot(x, 'm-*')
plt.xticks(range(len(x)), ['a', 'b', 'c', 'd', 'e', 'f'])
plt.yticks(range(0, 9, 2))
plt.title('Приклад 5 — Мітки осей')
plt.grid(True)
plt.savefig('example5.png', dpi=200)
plt.show()


# === Індивідуальне завдання — Варіант 12 ===
# Побудувати графік функції y = (5 * sin(10x) * sin(3x)) / x^x на проміжку (0, 8]

x = np.linspace(0.01, 8, 1000)  # уникаємо x=0
y = (5 * np.sin(10 * x) * np.sin(3 * x)) / (x ** x)

plt.plot(x, y, 'c-', label='(5·sin(10x)·sin(3x)) / x^x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Індивідуальне завдання — Варіант 12')
plt.grid(True)
plt.legend()
plt.savefig('variant12.png', dpi=200)
plt.show()
