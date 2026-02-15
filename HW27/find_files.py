# Скрипт, который принимает на вход список файлов и находит файлы, имена которых
# содержат определённую подстроку

# Функция поиска файлов, имена которых содержат заданную подстроку.
def find_files(file_list, condition):
    finding_files = []
    for file_name in file_list:
        if condition in file_name:
            finding_files.append(file_name)
    return finding_files

# Взял часть файлов из домашней директории пользователя в виде списка
files = ['conf','gtk-4.0','ubuntu-xdg-terminals.list','evolution','update-notifier','gnome-initial-setup-done','user-dirs.dirs','gnome-session','nautilus','user-dirs.locale','GNOME-xdg-terminals.list','pulse','xdg-terminals.list','gtk-3.0','tiling-assistant']
#  Запрашиваем условие для поиска
condition = input("Введите условие для поиска в именах файлов: ").strip()
# Вызываем функцию и передаём ей список файлов и условие
result = find_files(files, condition)
# Выводим результат
print("Ваше условие найдено в именах следующих файлов: ")
print(result)
