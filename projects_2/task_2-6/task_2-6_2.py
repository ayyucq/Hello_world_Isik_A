donor = input("Введите группу крови донора (O, A, B, AB): ").upper()
recipient = input("Введите группу крови пациента (O, A, B, AB): ").upper()
if donor == recipient or donor == "O":
    print("Переливание возможно.")
elif donor in ["A", "B", "AB"] and recipient in ["O", "A", "B", "AB"]:
    print("Переливание невозможно.")
else:
    print("Ошибка: введена некорректная группа крови.")