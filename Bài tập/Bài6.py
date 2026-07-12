class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findCycleStart(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if fast is None or fast.next is None:
        return None

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3

start = findCycleStart(head)

if start:
    print("Nút bắt đầu chu trình:", start.data)
else:
    print("Không có chu trình")