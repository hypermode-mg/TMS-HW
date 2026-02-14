# Скрипт проверки доступности ip-адресов из файла ip_list.txt с помощью ping
# и пишет результат каждой проверки в ping_res.log

import subprocess

# Функция проверяет доступность IP‑адреса с помощью команды ping
def ping_ip(ip):
    result = subprocess.run(
        ['ping', '-c', '3', '-W', '2', ip],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.returncode == 0

# Функция читает IP‑адреса из файла, проверяет их доступность и записывает результат
def main(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            ip = line.strip()
            if ip:  # Пропускаем пустые строки
                is_reachable = ping_ip(ip)
                status = "Доступен" if is_reachable else "Недоступен"
                result_line = f"{ip} — {status}\n"
                f_out.write(result_line)
                print(result_line.strip())

# Файл со списком IP‑адресов
INPUT_FILE = "ip_list.txt"
# Файл для результатов
OUTPUT_FILE = "ping_res.log"

print(f"Начинаем проверку IP‑адресов из файла '{INPUT_FILE}'...")
main(INPUT_FILE, OUTPUT_FILE)
print(f"Проверка завершена. Результаты записаны в файл '{OUTPUT_FILE}'.")