name = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Па): ")
with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write("ОПЕРАТОР\t")
    file.write("ЗНАЧЕНИЕ\n")
    file.write(f"{name}\t")
    file.write(f"{pressure}")
print("Данные успешно сохранены в sensor_log.txt")