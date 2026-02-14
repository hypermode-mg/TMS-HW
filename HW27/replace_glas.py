# Скрипт, который принимает на вход строку и заменяет в ней все гласные 
# буквы на минус

def replace_glassym(text):
    # Английские и русские гласные (строчные и заглавные)
    glassym = "aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    result = ""
    for char in text:
        if char in glassym: # Если текущий символ входит в glassym,
            result += "-" # то добавляем к результату -
        else:
            result += char # Иначе просто добавляем к результату текущий символ
    return result

# Запрашиваем ввод исходной строки с клавиатуры
input_string = input("Введите строку: ")
# Вызываем функцию
output_string = replace_glassym(input_string)
# Выводим результат на экран
print("Результат:", output_string)