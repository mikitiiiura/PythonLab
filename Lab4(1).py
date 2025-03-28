# Завдання 1: Задано речення. Скласти програму, яка визначає і виводить на екран 
# речення, в якому слова розташовані в зворотному порядку (наприклад, речення «мама мила раму» 
# буде змінено на «раму мила мама»).

def splitString(string):
    x = len(string)
    i = 0
    words = []  # Список для зберігання слів
    start = 0   # Початковий індекс слова

    # Проходимо по кожному символу рядка
    while i < x:
        # Якщо знаходимо пробіл
        if string[i] == " ":
            # Додаємо слово до списку (від start до поточного індексу)
            if start != i:  # Перевіряємо, щоб уникнути додавання порожніх слів
                words.append(string[start:i])
            start = i + 1  # Оновлюємо початковий індекс для наступного слова
        i += 1

    # Додаємо останнє слово, якщо воно є
    if start < x:
        words.append(string[start:])

    return words


string = str(input("Ввести речення: "))

splitstring = splitString(string)

i = len(splitstring) - 1  # Починаємо з останнього індексу
reversestring=[]

while i >=0 :
    reversestring.append(splitstring[i])  # Додаємо слово до перевернутого списку
    i -= 1  # Зменшуємо індекс

# Збираємо перевернутий список слів назад у речення
result = " ".join(reversestring)

# Виводимо результат
print("Речення: ", result )