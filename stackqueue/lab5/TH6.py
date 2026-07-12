class DynamicArray:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self.resize()

        self.data[self.size] = value
        self.size += 1

    def resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data

    def display(self):
        print(self.data[:self.size])
        print("Capacity:", self.capacity)


arr = DynamicArray()

for i in range(1, 10):
    arr.append(i)
    arr.display()