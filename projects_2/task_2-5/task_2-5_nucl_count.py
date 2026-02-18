print("\n=== Анализ последовательности ДНК ===\n")
dna = input("Введите последовательность ДНК: ").upper()
print(f"\nПоследовательность в верхнем регистре: {dna}")
length_dna = len(dna)
percentage_A = (dna.count("A") * 100) / length_dna
percentage_T = (dna.count("T") * 100) / length_dna
percentage_G = (dna.count("G") * 100) / length_dna
percentage_C = (dna.count("C") * 100) / length_dna
print("\nПодсчёт нуклеотидов:")
print(f"A: {dna.count("A")} ({percentage_A}%)")
print(f"T: {dna.count("T")} ({percentage_T}%)")
print(f"G: {dna.count("G")} ({percentage_G}%)")
print(f"C: {dna.count("C")} ({percentage_C}%)")
print(f"\nОбщая длина: {length_dna}\n")