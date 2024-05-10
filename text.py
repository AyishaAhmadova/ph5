class NumberManipulator:
    def __init__(self):
        self.mylist = []

    def add_numbers(self, numbers):
        self.mylist.extend(numbers)

    def find_indexes_of_sum(self, hedef):
        indexler = []
        for i in range(len(self.mylist)):
            for j in range(i + 1, len(self.mylist)):
                if self.mylist[i] + self.mylist[j] == hedef:
                    indexler.append((i, j))
        if indexler:
            return indexler
        else:
            return -1

manipulator = NumberManipulator()
manipulator.add_numbers([1, 2, 3, 4, 5])
hedef = 7
print("Hədəfə bərabər olan cütlerin indeksləri:", manipulator.find_indexes_of_sum(hedef))