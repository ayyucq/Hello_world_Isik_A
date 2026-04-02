#!/bin/bash
printf "%-20s %-8s %-8s %-8s %-8s\n" "Файл" "A" "T" "G" "C"
echo "--------------------------------------------------------"
for file in *.fasta; do
    if [ ! -f "$file" ]; then
        echo "Файлы .fasta не найдены."
        exit 1
    fi
    if [ ! -s "$file" ]; then
        continue
    fi
    sequence=$(grep -v "^>" "$file" | tr -d '\n')
    count_A=$(echo "$sequence" | grep -o "A" | wc -l)
    count_T=$(echo "$sequence" | grep -o "T" | wc -l)
    count_G=$(echo "$sequence" | grep -o "G" | wc -l)
    count_C=$(echo "$sequence" | grep -o "C" | wc -l)
    printf "%-20s %-8s %-8s %-8s %-8s\n" \
        "$file" \
        "$(echo $count_A | xargs)" \
        "$(echo $count_T | xargs)" \
        "$(echo $count_G | xargs)" \
        "$(echo $count_C | xargs)"
done
echo "--------------------------------------------------------"
echo "Подсчет завершен."
