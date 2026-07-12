class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity
        self.cost = 0

    def append(self, value):
        if self.size == self.capacity:
            old = self.data
            self.capacity *= 2
            self.data = [None] * self.capacity

            for i in range(self.size):
                self.data[i] = old[i]
                self.cost += 1

        self.data[self.size] = value
        self.size += 1
        self.cost += 1

    def display(self):
        print(self.data[:self.size])


n = int(input("Nhập n: "))

arr = DynamicArray()

for i in range(n):
    arr.append(i)

arr.display()
print("Tổng chi phí:", arr.cost)
print("Chi phí trung bình:", arr.cost / n)