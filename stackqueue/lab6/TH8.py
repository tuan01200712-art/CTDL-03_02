class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def hasCycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

head.next.next.next.next = head.next

if hasCycle(head):
    print("Danh sách có chu trình")
else:
    print("Danh sách không có chu trình")