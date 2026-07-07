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
    
    def append(self, value):
        self.data.append(value)

    def popback(self):
        if len(self.data) == 0:
            return "Danh sách rỗng"
        return self.data.pop()
    
arr = ArrayList()

arr.add(1)
arr.add(2)
arr.add(3)
x = arr.popback()
print("danh sách đã xóa ", arr.data)