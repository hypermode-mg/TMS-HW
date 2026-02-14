# Скрипт, который принимает от пользователя строку и выводит на экран 
# количество букв в верхнем регистре, количество букв в нижнем регистре,
# количество цифр и количество символов пунктуации

import string

# Основняа функция анализа строки
def analyze_string(input_string):
    # Инициализируем счётчики
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    punctuation_count = 0

    # Проходим по каждому символу в строке
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in string.punctuation:
            punctuation_count += 1

    # Выводим результаты
    print(f"Количество букв в верхнем регистре: {uppercase_count}")
    print(f"Количество букв в нижнем регистре: {lowercase_count}")
    print(f"Количество цифр: {digit_count}")
    print(f"Количество символов пунктуации: {punctuation_count}")

# Получаем строку от пользователя
user_input = input("Введите строку: ")
# Вызываем функцию анализа строки
analyze_string(user_input)