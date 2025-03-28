# Задано текст з цифр і літер латинського алфавіту. Скласти програму, 
# яка визначає, яких літер – голосних {a, e, i, o, u, y} або приголосних більше в цьому тексті.

vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

consonants = [
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 
    'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z'
]

#textTest ="Lorem nipel = 325"

# Отримуємо текст від користувача
text = input("Введіть текст: ")

# Ініціалізуємо лічильники
vowels_count = 0
consonants_count = 0

# Проходимо по кожному символу тексту
for char in text:
    upper_char = char.upper()  # Переводимо символ у верхній регістр
    if upper_char in vowels:  # Перевіряємо, чи є символ голосною
        vowels_count += 1
    elif upper_char in consonants:  # Перевіряємо, чи є символ приголосною
        consonants_count += 1

print("Голосних літер", vowels_count)

print("Приголосних літер", consonants_count)

if(vowels_count > consonants_count):
    print("Голосних літер більше аніж приголосних")
else:
    print("Приголосних літер більше аніж голосних")