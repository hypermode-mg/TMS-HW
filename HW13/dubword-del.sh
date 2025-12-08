#!/usr/bin/env bash
# Скрипт для удаления повторов строк в тексте
# Использование ./dubword-del.sh input.txt > output.txt

set -euo pipefail
export LC_ALL=ru_RU.UTF-8

if [[ "${1:-}" == "-i" ]]; then
  inplace=true
  infile="${2:-}"
else
  inplace=false
  infile="${1:-}"
fi

if [[ -z "$infile" || ! -f "$infile" ]]; then
  echo "Usage: $0 [-i] input.txt" >&2
  exit 1
fi

process() {
  # awk: для каждой строки разбивает по пробельным символам,
  # сравнивает слова в lower-case и выводит первое вхождение последовательности
  awk '
  {
    out = ""
    prev = ""
    for (i = 1; i <= NF; ++i) {
      word = $i
      lw = tolower(word)
      if (lw != prev) {
        if (out == "") out = word
        else out = out " " word
      }
      prev = lw
    }
    # Если строка была пустой (NF==0), сохранить пустую строку
    if (NF == 0) print ""
    else print out
  }
  ' FS="[ \t\n\r]+" OFS=" " "$1"
}

if $inplace; then
  tmp="$(mktemp)"
  process "$infile" > "$tmp" && mv "$tmp" "$infile"
else
  process "$infile"
fi