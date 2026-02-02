# Используем последний образ Alpine
FROM alpine:latest

COPY app.sh /app.sh
RUN apk update && apk upgrade && apk add iputils-ping && chmod +x /app.sh
CMD ["/app.sh"]

