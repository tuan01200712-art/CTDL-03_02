class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return

            index = (index + 1) % self.size

        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]

            index = (index + 1) % self.size

        return None

    def remove(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return True

            index = (index + 1) % self.size

        return False

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


ht = HashTable(5)

ht.put("a", 1)
ht.put("b", 2)
ht.put("c", 3)
ht.put("f", 6)

print("a =", ht.get("a"))
print("b =", ht.get("b"))

ht.remove("b")

ht.display()