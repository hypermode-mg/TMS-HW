# Скрипт, который принимает на вход список чисел и находит медиану этих чисел

# Функция поиска файлов, имена которых содержат заданную подстроку.
def find_files(file_list, condition):
    finding_files = []
    for file_name in file_list:
        if condition in file_name:
            finding_files.append(file_name)
    return finding_files

# Пример использования
files = ['conf','gtk-4.0','ubuntu-xdg-terminals.list','evolution','update-notifier','gnome-initial-setup-done','user-dirs.dirs','gnome-session','nautilus','user-dirs.locale','GNOME-xdg-terminals.list','pulse','xdg-terminals.list','gtk-3.0','tiling-assistant']
condition = input("Введите условие для поиска в именах файлов: ").strip()
result = find_files(files, condition)
print("Ваше условие найдено в именах следующих файлов: ")
print(result)