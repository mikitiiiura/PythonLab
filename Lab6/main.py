from list_operations import (
    sort_list, search_element, search_subsequence,
    find_min_five, find_max_five, calculate_average, remove_duplicates
)

# Початковий список
numbers = [5, 3, 8, 6, 2, 8, 10, 3, 4, 1, 7, 9, 2, 5, 10, 6]

# Використання функцій
sorted_numbers = sort_list(numbers)
element_index = search_element(numbers, 6)
subseq_index = search_subsequence(numbers, [3, 8])
min_five = find_min_five(numbers)
max_five = find_max_five(numbers)
average = calculate_average(numbers)
unique_list = remove_duplicates(numbers)

# Вивід результатів
print("Оригінальний список:", numbers)
print("Відсортований список:", sorted_numbers)
print(f"Індекс елемента '6': {element_index}")
print(f"Індекс послідовності [3, 8]: {subseq_index}")
print("Перші 5 мінімальних чисел:", min_five)
print("Перші 5 максимальних чисел:", max_five)
print("Середнє арифметичне:", average)
print("Список без дублікатів:", unique_list)
