choice = input("Choose a path (left / right / straight): ").lower()
if choice == "left":
    print("Ты потеряешь коня, но останешься жив.")
elif choice == "right":
    print("Ты найдёшь богатство, но пройдёшь через испытания.")
elif choice == "straight" or choice == "forward":
    print("Ты станешь героем, но погибнешь.")
else:
    print("Invalid choice.")