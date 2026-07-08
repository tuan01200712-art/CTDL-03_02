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
    else:
        return None

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.next.next.next.next.next = head.next.next

start = findCycleStart(head)

if start:
    print("Điểm bắt đầu chu trình là:", start.data)
else:
    print("Danh sách không có chu trình")