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