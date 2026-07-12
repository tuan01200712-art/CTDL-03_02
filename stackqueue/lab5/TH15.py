class ArrayList:
    def __init__(self):
        self.data = []
        self.modCount = 0

    def add(self, value):
        self.data.append(value)
        self.modCount += 1

    def remove(self, value):
        self.data.remove(value)
        self.modCount += 1

    def __iter__(self):
        return ArrayListIterator(self)


class ArrayListIterator:
    def __init__(self, arr):
        self.arr = arr
        self.index = 0
        self.expectedModCount = arr.modCount

    def __iter__(self):
        return self

    def __next__(self):
        if self.expectedModCount != self.arr.modCount:
            raise RuntimeError("List da bi thay doi trong khi dang duyet")

        if self.index >= len(self.arr.data):
            raise StopIteration

        value = self.arr.data[self.index]
        self.index += 1
        return value


a = ArrayList()
a.add(1)
a.add(2)
a.add(3)

try:
    for x in a:
        print(x)
        if x == 2:
            a.add(4)
except RuntimeError as e:
    print("Loi:", e)