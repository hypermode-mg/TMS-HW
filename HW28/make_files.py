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