#!/bin/sh

LOG=/data/logs/ping.log

echo "Пингуем docker-nginx1" >> $LOG
ping -c 10 docker-nginx1 >> $LOG
