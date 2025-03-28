import random

def generate_list(n):
    return [random.randint(-10, 10) for _ in range(n)]

def sum_between_negatives(lst):
    neg_indices = [i for i, x in enumerate(lst) if x < 0]

    if len(neg_indices) < 2:
        print("У списку менше двох від’ємних чисел!")
        return None

    first, second = neg_indices[0], neg_indices[1]
    return sum(lst[first + 1:second])

n = int(input("Введіть кількість елементів списку: "))
random_list = generate_list(n)
print("Згенерований список:", random_list)

result = sum_between_negatives(random_list)
if result is not None:
    print("Сума між першим і другим від’ємними числами:", result)
