class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            # print(self.numberOfFloors, other.numberOfFloors)
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        return False


building_1 = Building(5, "жилой дом")
building_2 = Building(10, "офисное здание")
building_3 = Building(5, "жилой дом")

# Сравнение объектов
print(building_1 == building_2)  # False
print(building_1 == building_3)  # True
