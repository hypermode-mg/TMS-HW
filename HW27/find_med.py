# Скрипт, который принимает на вход список чисел и находит медиану этих чисел

# Для упрощения импортируем модуль statistics
import statistics

# Функция находит медиану списка чисел с помощью модуля statistics
def find_median(numbers):
    return statistics.median(numbers)

# Запрашиваем ввод данных с клавиатуры
print("Введите числа через пробел:")
user_input = input()

# Преобразуем введённую строку в список чисел
numbers = list(map(float, user_input.split()))

# Находим медиану и выводим на экран
median = find_median(numbers)
print(f"Медиана: {median}")