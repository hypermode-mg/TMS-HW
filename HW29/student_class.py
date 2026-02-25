# Работаем с классом студентов и их атрибутами

# Создаём класс Студент и задаём его атрибуты
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  # Список оценок студента

# Задаём методы работы с атрибутами класса
# Метод для вычисления среднего балла студента.
    def calc_avg_score(self):
        if len(self.grades) == 0:
            return 0
        avg_score = sum(self.grades) / len(self.grades)
        return round(avg_score, 2)

#Метод для определения статуса студента: отличник, хорошист, троечник.
    def status_def(self):
        avg_score = self.calc_avg_score()
        if avg_score >= 4.5:
            return "отличник"
        elif avg_score >= 3.5:
            return "хорошист"
        else:
            return "троечник"

# Метод для вывода информации о студенте.
    def disp_info(self):
	# Вызываем метод для вычисления среднего балла
        avg_score = self.calc_avg_score()
	# Вызываем метод для определения статуса
        status = self.status_def()
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age} лет")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {avg_score}")
        print(f"Статус: {status}\n")


# Создание нескольких объектов класса "Студент"
student1 = Student("Иван Петров", 19, [5, 5, 4, 5, 5, 4, 5])
student2 = Student("Елизавета Краснова", 20, [4, 3, 4, 5, 4, 5])
student3 = Student("Пётр Иванов", 18, [4, 4, 3, 2, 3, 3, 4, 3])

# Вызываем метод для вывода информации о каждом студенте
student1.disp_info()
student2.disp_info()
student3.disp_info()