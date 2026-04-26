def print_status(ecosystem):
    print(f"\n--- День {ecosystem.day} ---")
    print(f"  Зайцев: {ecosystem.rabbits.count()}")
    print(f"  Лис:    {ecosystem.foxes.count()}")

def print_result(ecosystem):
    print("\n=== Симуляция завершена ===")
    if ecosystem.rabbits.count() == 0:
        print("Все зайцы вымерли. Победили лисы!")
    elif ecosystem.foxes.count() == 0:
        print("Все лисы вымерли. Зайцы выжили!")
    print(f"Длилось дней: {ecosystem.day}")
