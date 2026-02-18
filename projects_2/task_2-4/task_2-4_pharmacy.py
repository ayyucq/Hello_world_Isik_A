num_capsules_produced = int(input("Введите общее количество произведенных капсул: "))
num_capsules_package = int(input("Введите количество капсул в одной упаковке: "))
full_packages = num_capsules_produced//num_capsules_package
remaining_capsules = num_capsules_produced%num_capsules_package
ramka = (
    "--- Отчет фасовочного цеха ---\n"
    f"Полных упаковок:\t{full_packages}\n"
    f"Остаток капсул:\t\t{remaining_capsules}\n"
)
print(ramka)