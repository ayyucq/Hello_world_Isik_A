#!/bin/bash
read -p "Введите ваш вес (кг): " weight
read -p "Введите ваш рост (м): " height
bmi=$(echo "$weight / ($height * $height)" | bc)
bmi_int=$(printf "%.0f" $bmi)
echo "Ваш индекс массы тела (ИМТ): $bmi_int"
