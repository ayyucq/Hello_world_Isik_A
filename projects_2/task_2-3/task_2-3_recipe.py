name = input("Введите название питательной среды: ")
concentration = input("Введите концентрацию агара (%): ")
temperature = input("Введите температуру стерилизации (°C): ")
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"Название питательной среды: {name}\n")
    file.write(f"Концентрацию агара (%): {concentration}\n")
    file.write(f"Температуру стерилизации: {temperature}\n")
    file.close()
print("Файл 'recipe.txt' успешно сформирован!")