class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findMiddle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("null")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Danh sách:")
printList(head)

middle = findMiddle(head)
print("Nút giữa là:", middle.data)