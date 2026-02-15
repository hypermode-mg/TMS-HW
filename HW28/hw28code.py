# Задание 1
# Программа вычисления произведения двух чисел через функцию

def multiply_numbers(a,b):
    return a * b

# Запрашиваем ввод чисел у пользователя
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Выводим результат произведения на экран
print(f"Произведение этих чисел =",multiply_numbers(a,b))

# Задание 2
# Программа для создания текстового файла с заданным именем и содержимым
# и выводом содержимого на экран

import subprocess

# Задаём содержимое файла
test_text = "Это тестовый файл для домашнего задания по программированию\n"

# Записываем содержимое в файл
with open('test.txt', 'w', encoding='utf-8') as file:
    file.write(test_text)

# Открываем файл для просмотра с помощью cat
print("Содержимое файла test.txt:")
subprocess.run(['cat', 'test.txt'])

# Задание 3
# Программа для создания каталога, 3 пустых файлов в нём и вывода на экран
# содержимого этого каталога

import os

# Создаём каталог mydir в текущей директории
os.makedirs('mydir', exist_ok=True)

# Переходим в созданный каталог
os.chdir('mydir')

# Создаём пустые файлы
open('test1.txt', 'w').close()
open('test2.txt', 'w').close()
open('test3.txt', 'w').close()

# Получаем и выводим содержимое каталога
print("Содержимое каталога mydir:")
print('\n'.join(os.listdir('.')))
# Возвращаемся в рабочий каталог
os.chdir('..')

# Задание 4
# Программа для создания списка пользователей с использованием шаблона Jinja2

from jinja2 import Environment, FileSystemLoader

# Создаём список пользователей
users_list = [
    {"name": "Андрей", "email": "andrey@mail.ru"},
    {"name": "Любовь", "email": "love@mail.ru"},
    {"name": "Иван", "email": "ivan@mail.ru"},
    {"name": "Михаил", "email": "mikhail@mail.ru"},
    {"name": "Мария", "email": "masha@mail.ru"}
]

# Указываем папку с шаблонами
env = Environment(loader=FileSystemLoader('templates/'))

# Загружаем шаблон
template = env.get_template('template.html')

# Передаём список пользователей в шаблон и рендерим HTML
rendered_html = template.render(users=users_list)

# Выводим результат на экран
print(rendered_html)