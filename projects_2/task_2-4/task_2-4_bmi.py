height_cm = float(input("Введите ваш рост (см): "))
weight = float(input("Введите ваш вес (кг): "))
height_m = height_cm/100 
bmi = weight/(height_m**2)
ramka = (
    "--- Отчет о состоянии здоровья ---\n"
    f"Рост:\t{height_cm} см\n"
    f"Вес:\t{weight} кг\n"
    f"Индекс массы тела:\t{bmi:.2f}\n"
)
print(ramka)