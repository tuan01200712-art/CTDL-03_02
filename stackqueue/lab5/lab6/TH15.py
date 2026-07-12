class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addNode(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.addNode(node)

            if len(self.cache) > self.capacity:
                tail = self.removeTail()
                del self.cache[tail.key]


cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))

cache.put(3, 30)

print(cache.get(2))
print(cache.get(3))

cache.put(4, 40)

print(cache.get(1))
print(cache.get(3))
print(cache.get(4))