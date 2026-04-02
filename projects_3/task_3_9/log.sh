#!/bin/bash
LOG_FILE="report.log"
ERROR_CODE=2
if [ -e "$LOG_FILE" ]; then
    echo "✓ Лог-файл $LOG_FILE существует."
else
    echo "✗ Лог-файл $LOG_FILE не существует. Создаю..."
    touch "$LOG_FILE"
    echo "Файл $LOG_FILE создан."
fi
echo ""
echo "Анализ кода ошибки: $ERROR_CODE"
if [ "$ERROR_CODE" -eq 0 ]; then
    echo "Статус: УСПЕШНО. Ошибок не обнаружено."
elif [ "$ERROR_CODE" -eq 1 ]; then
    echo "Статус: ПРЕДУПРЕЖДЕНИЕ. Обнаружены незначительные ошибки."
elif [ "$ERROR_CODE" -eq 2 ]; then
    echo "Статус: КРИТИЧЕСКАЯ ОШИБКА. Требуется вмешательство."
else
    echo "Статус: НЕИЗВЕСТНЫЙ КОД ОШИБКИ ($ERROR_CODE)"
fi
