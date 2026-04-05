#!/bin/bash
cat > students.txt << 'DATA'
Ivan 78
Maria 92
Oleg 67
Anna 85
DATA
echo "=== Только имена студентов ==="
awk '{print $1}' students.txt
echo ""
echo "=== Только оценки ==="
awk '{print $2}' students.txt
echo ""
echo "=== Номер строки и имя ==="
awk '{print NR, $1}' students.txt
