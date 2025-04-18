# === Лабораторна робота №14 ===
# Варіант 12
# Побудова 3D графіків та анімацій

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from math import *
import string
from collections import Counter
import matplotlib as mpl
import pylab

# -------------------------------
# 🔸 ЗАВДАННЯ 1: ГІСТОГРАМА ЛІТЕР
# -------------------------------

print("\n🔸 ЗАВДАННЯ 1: ГІСТОГРАМА ЛІТЕР З ФАЙЛУ\n")

try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read().lower()
except FileNotFoundError:
    print("❌ Файл 'text.txt' не знайдено! Створіть файл у тій же папці з текстом для аналізу.")
    text = "тестовий текст для прикладу histogram example text"

filtered_text = [char for char in text if char in string.ascii_lowercase or char in 'абвгґдеєжзииіїйклмнопрстуфхцчшщьюя']
letter_counts = Counter(filtered_text)
letters = list(letter_counts.keys())
frequencies = list(letter_counts.values())

plt.figure(figsize=(12, 6))
plt.bar(letters, frequencies, color='skyblue')
plt.title('Частота появи літер у тексті')
plt.xlabel('Літери')
plt.ylabel('Кількість')
plt.grid(True, axis='y')
plt.show()


# -----------------------------------------------------
# 🔹 ЗАВДАННЯ 2: АНІМАЦІЯ ФУНКЦІЇ З ЛР13 (варіант 12)
# -----------------------------------------------------

print("\n🔹 ЗАВДАННЯ 2: АНІМАЦІЯ ФУНКЦІЇ (5·sin(10x)·sin(3x)) / x^x\n")

def func(x):
    return (5 * np.sin(10 * x) * np.sin(3 * x)) / (x ** x)

x = np.linspace(0.01, 8, 1000)
y = func(x)

fig, ax = plt.subplots()
line, = ax.plot([], [], 'c-', label='(5·sin(10x)·sin(3x)) / x^x')
ax.set_xlim(0, 8)
ax.set_ylim(-4, 4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Анімована побудова графіка')
ax.grid(True)
ax.legend()

xdata, ydata = [], []

def init():
    line.set_data([], [])
    return line,

def update(frame):
    xdata.append(x[frame])
    ydata.append(y[frame])
    line.set_data(xdata, ydata)
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True, interval=5, repeat=False)
plt.show()


# -------------------------------------------------
# 🔸 ПРИКЛАД 1: Побудова тривимірної параметричної кривої
# -------------------------------------------------

# -------------------------------------------------
# 🔸 ПРИКЛАД 1: Побудова тривимірної параметричної кривої
# -------------------------------------------------

print("\n🔸 ПРИКЛАД 1: 3D параметрична крива\n")

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # ← Ось тут виправлено

theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, label='Параметрична крива')
ax.legend()
plt.show()



# ----------------------------------------------------
# 🔹 ПРИКЛАД 2: Побудова графіка функції z=sin(0.3x)*cos(0.75y)
# ----------------------------------------------------

print("\n🔹 ПРИКЛАД 2: Графік функції z=sin(0.3x)*cos(0.75y)\n")

def makeData():
    x = np.arange(-10, 10, 0.5)
    y = np.arange(-10, 10, 0.5)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = np.sin(xgrid * 0.3) * np.cos(ygrid * 0.75)
    return xgrid, ygrid, zgrid

x, y, z = makeData()
fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis')
pylab.show()


# -------------------------------------------------
# 🔸 ПРИКЛАД 3: Побудова 3D поверхні (сфера)
# -------------------------------------------------

print("\n🔸 ПРИКЛАД 3: Побудова 3D поверхні (сфера)\n")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, color='b')
plt.show()


# ----------------------------------------------------------
# 🔹 ПРИКЛАД 4: Анімована побудова графіка функції y = sin(2πt)e^(-t/10)
# ----------------------------------------------------------

print("\n🔹 ПРИКЛАД 4: Анімована побудова графіка y = sin(2πt) * e^(-t/10)\n")

def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1
        yield t, sin(2 * pi * t) * exp(-t / 10.)

def init_anim():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

def run(data):
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    if t >= xmax:
        ax.set_xlim(xmin, 2 * xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10, repeat=False, init_func=init_anim)
plt.show()
