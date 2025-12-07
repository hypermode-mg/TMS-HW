#!/bin/bash
# Скрипт для вывода на консоль размера и прав каждого файла в заданном каталоге
# Проверяем наличие аргумента
if [ $# -ne 1 ]; then
  echo "Использование: $0 <каталог>"
  exit 1
fi

directory="$1"

# Проверяем существование каталога
if [ ! -d "$directory" ]; then
  echo "Ошибка: каталог '$directory' не существует."
  exit 1
fi

# Цикл for для всех файлов в каталоге (рекурсивно)
for file in $(find "$directory" -type f); do
  size=$(stat -c%s "$file")          # размер файла в байтах
  perms=$(stat -c%A "$file")         # права доступа в формате rwxr-xr-x
  echo "Файл: $file | Размер: $size байт | Права: $perms"
done