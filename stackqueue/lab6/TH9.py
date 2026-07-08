class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    if l1 is not None:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next


def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("null")


a = Node(1)
a.next = Node(3)
a.next.next = Node(5)

b = Node(2)
b.next = Node(4)

c = merge(a, b)

print("Danh sách sau khi trộn:")
printList(c)