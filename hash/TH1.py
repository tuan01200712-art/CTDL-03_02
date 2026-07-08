class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def remove(self, key):
        index = self.hash_function(key)

        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                self.table[index].pop(i)
                return True

        return False

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


ht = HashTable(5)

ht.put("a", 1)
ht.put("b", 2)
ht.put("c", 3)
ht.put("f", 6)

print(ht.get("a"))
print(ht.get("b"))

ht.remove("b")

ht.display()