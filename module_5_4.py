class Building:
    total = 0

    def __init__(self):
        Building.total += 1

#    def __str__(self):
#       return str(Building.total)

# Создаем 40 объектов класса Building
buildings = []
for i in range(40):
    buildings.append(Building())

# Выводим объекты на экран
for building in buildings:
    print(building)

# Выводим общее количество созданных объектов
print("Всего создано объектов Building:", Building.total)