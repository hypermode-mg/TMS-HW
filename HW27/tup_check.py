# Скрипт который принимает на вход от пользователя кортеж и проверяет, 
# все ли его элементы являются уникальными

# Функция проверки
def all_uniq(tup):
    check_set = set()
    for item in tup:
        if item in check_set:
            return False
        check_set.add(item)
    return True

# Запрос ввода элементов  у пользователя
print("Введите элементы кортежа через пробел:")
user_input = input().strip()

# Если ввод не пустой, разбиваем на элементы и создаём кортеж 
if user_input:
    tup = tuple(user_input.split())
# иначе — пустой кортеж
else:
    tup = tuple()

# Проверка уникальности элементов и вывод результата
if all_uniq(tup):
    print("Все элементы уникальны")
else:
    print("Не все элементы уникальны")