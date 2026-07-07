class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def pushBack(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def popFront(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def popBack(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def printForward(self):
        cur = self.head
        while cur:
            print(cur.data, end=" <-> ")
            cur = cur.next
        print("null")

    def printBackward(self):
        cur = self.tail
        while cur:
            print(cur.data, end=" <-> ")
            cur = cur.prev
        print("null")


dll = DoublyLinkedList()

dll.pushFront(2)
dll.pushFront(1)
dll.pushBack(3)
dll.pushBack(4)

print("Duyệt xuôi:")
dll.printForward()

print("Duyệt ngược:")
dll.printBackward()

dll.popFront()
dll.popBack()

print("Sau khi xóa đầu và cuối:")
dll.printForward()