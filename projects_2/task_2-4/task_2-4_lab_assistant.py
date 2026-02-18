volume = float(input("Введите нужный объем раствора (в мл): "))
salt_mass = volume * 0.009
salt_mass = round(salt_mass, 2)
water_volume = volume
report = (
    "ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n"
    "-----------------------\n"
    f"Общий объем: {volume:.0f} мл\n"
    f"Масса соли:  {salt_mass:.2f} г\n"
    f"Объем воды:  {water_volume:.0f} мл\n"
)
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(report)
print("Рецепт сохранен в файл recipe.txt")