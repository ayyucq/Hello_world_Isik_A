#!/bin/bash
for i in {1..20}; do
    if [ $i -eq 15 ]; then
        echo "Число 15 встречено. Останавливаю цикл."
        break
    fi
    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi
    echo "Нечетное число: $i"
done
echo "Цикл завершен."
