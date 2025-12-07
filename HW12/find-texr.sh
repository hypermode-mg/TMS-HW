#!/bin/bash
# Скрипт для поиска заданной строки во всех файлах заданного каталога
# Проверяем наличие двух аргументов
if [ $# -ne 2 ]; then
  echo "Использование: $0 <строка_для_поиска> <каталог>"
  exit 1
fi

search_str="$1"
directory="$2"

function search_dir() {
  local dir="$1"
# Проверяем наличие доступа к заданому каталогу
  if [ ! -r "$dir" ]; then
    echo "Ошибка: нет доступа к каталогу '$dir'"
    return
  fi

  # Перебираем содержимое каталога
  for entry in "$dir"/*; do
    if [ -d "$entry" ]; then
      # Рекурсивный вызов для подкаталога
      search_dir "$entry"
    elif [ -f "$entry" ]; then
      # Проверяем наличие строки в файле
      if grep -q -- "$search_str" "$entry" 2>/dev/null; then
        size=$(stat -c%s "$entry" 2>/dev/null)
        echo "Файл: $entry | Размер: $size байт"
      fi
    fi
  done
}

search_dir "$directory"