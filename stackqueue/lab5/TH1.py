class ArrayList:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return "Index không hợp lệ"

    def set(self, index, value):
        if 0 <= index < len(self.data):
            self.data[index] = value
        else:
            print("Index không hợp lệ")

    def size(self):
        return len(self.data)


arr = ArrayList()

arr.add(1)
arr.add(2)
arr.add(3)

print("Danh sách:", arr.data)
print("get(1) =", arr.get(1)) 

arr.set(1, 10)
print("Sau khi set(1, 10):", arr.data)

print("size() =", arr.size())