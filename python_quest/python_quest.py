def generate_report(error_count, avg_cpu, offline_servers):
    print("==== ОТЧЁТ ====")
    print(f"Ошибок: {error_count}")
    print(f"Средняя загрузка CPU: {aver_usage:.2f}")
    print("Серверы со статусом 'offline':")
    print(offline_servers)

print("Разбор логов")
logs = [
    "INFO: Service started",
    "ERROR: Connection timeout",
    "WARNING: CPU usage high",
    "ERROR: Disk full",
    "INFO: Health check passed",
    "ERROR: Out of memory"
]

# 1. Считаем количество ошибок
error_count = sum("ERROR" in log for log in logs)

# 2. Получаем список только ошибок
errors = [log for log in logs if "ERROR" in log]

# 3. Выводим сообщение
if error_count > 2:
    message = "Срочно чиним прод!"
else:
    message = "Пока держимся"

# Вывод результатов
print(f"Количество ошибок: {error_count}")
print("Список ошибок:")
for error in errors:
    print(f"  - {error}")
print(message)

print("\nРазбор нагрузки на ЦПУ")

cpu_usage = [35, 55, 78, 90, 67, 120, 15]

# Удаляем значения больше 100, т.к. они не достоверные
true_cpu_usage = [value for value in cpu_usage if value <= 100]

# 1. Находим максимальное значение (среди оставшихся)
max_usage = max(true_cpu_usage)
print(f"Максимальное значение: {max_usage}")

# 2. Находим среднюю загрузку (среди оставшихся)
aver_usage = sum(true_cpu_usage) / len(true_cpu_usage)
print(f"Средняя загрузка: {aver_usage:.2f}")

# 3. Выводим список значений больше 80 (среди оставшихся)
usage_gt_80 = [value for value in true_cpu_usage if value > 80]
print(f"Значения больше 80: {usage_gt_80}")

# 4. Проверяем наличие значений больше 100 в исходных данных
if any(value > 100 for value in cpu_usage):
    print("Некорректные данные мониторинга!")

print("\nАнализ серверов онлайн")
servers = [
    ("web-1", "online"),
    ("web-2", "offline"),
    ("db-1", "online"),
    ("cache-1", "offline"),
    ("cache-1", "offline")
]

# 1. Выводим имена серверов со статусом "offline"
print("Серверы со статусом 'offline':")
offline_servers = []
for name, status in servers:
    if status == "offline":
        offline_servers.append(name)
        print(name)

# 2. Считаем количество онлайн‑серверов
online_count = sum(1 for _, status in servers if status == "online")
print(f"\nКоличество онлайн‑серверов: {online_count}")

# Проверяем условие и выводим предупреждение при необходимости
if online_count < 2:
    print("Риск падения сервиса!")

generate_report(error_count, aver_usage,offline_servers)