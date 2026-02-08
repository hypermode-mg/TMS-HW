FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Обновление и установка nginx и curl
RUN apt-get update && apt-get install -y nginx curl && rm -rf /var/lib/apt/lists/*

# Создание каталога /app/static внутри контейнера
RUN mkdir -p /app/static

# Копирование файла конфигурации nginx (из контекста сборки)
# Предполагается, что локально файл называется nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

# Копирование содержимого локального каталога ./app/static в /app/static контейнера
# Предполагается, что в контексте сборки есть папка app/static
COPY app/static /app/static

# Открываем порт 8080
EXPOSE 8080

# Запуск nginx в форграунд режиме с указанием конфигурационного файла
# Используем параметр -g "daemon off;" чтобы nginx не уходил в фон
CMD ["nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]
