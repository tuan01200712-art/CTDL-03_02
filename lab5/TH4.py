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
    
    def insert(self, index ,value):
        self.data.append(0)
        for i in range(len(self.data)-1, index, -1):
            self.data[i] = self.data[i-1]
        
        self.data[index] = value

    def indexOf(self, value):
        for i in range(len(self.data)):
            if self.data[i] == value:
                return i
        return -1 
arr = ArrayList()
arr.data = [5, 3, 7]

print("Giá trị là:", arr.indexOf(7))   