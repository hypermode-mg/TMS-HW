# Работаем с классом Книга и его атрибутами

# Создаём класс "Книга" и инициализируем его атрибуты
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Метод для получения названия книги
    def get_title(self):
        return self.title

    # Метод для изменения названия книги
    def set_title(self, new_title):
        self.title = new_title

    # Метод для получения автора книги
    def get_author(self):
        return self.author

    # Метод для изменения автора книги
    def set_author(self, new_author):
        self.author = new_author

    # Метод для получения года издания книги
    def get_year(self):
        return self.year

    # Метод для изменения года издания книги
    def set_year(self, new_year):
        self.year = new_year

    # Метод для вывода информации о книге
    def info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год издания: {self.year}"


# Создаём несколько объектов класса "Книга"
Книга1 = Book("Война и мир", "Лев Толстой", 1869)
Книга2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866)
Книга3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1966)

# Вызываем метод info для получения всей информации о каждом объекте
print("Исходная информация о книгах:")
print(Книга1.info())
print(Книга2.info())
print(Книга3.info())

# Изменяем атрибуты через методы set_
Книга1.set_title("Война и мир. Том 1-4")
Книга2.set_author("Ф. М. Достоевский")
Книга3.set_year(1967)

# Вызываем метод info для получения обновлённой информации о каждом объекте
print("\nИнформация о книгах после изменений:")
print(Книга1.info())
print(Книга2.info())
print(Книга3.info())

# Получаем отдельные атрибуты книг через методы get_
print(f"\nНазвание первой книги: {Книга1.get_title()}")
print(f"Автор второй книги: {Книга2.get_author()}")
print(f"Год издания третьей книги: {Книга3.get_year()}")