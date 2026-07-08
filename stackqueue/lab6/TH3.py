class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def pushFront(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def pushBack(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = newNode

    def printList(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("null")
    def search(self, x):
        index = 0
        cur = self.head

        while cur:
            if cur.data == x:
                return index
            cur = cur.next
            index += 1

        return -1

lst = SinglyLinkedList()
print(lst.search(5))
