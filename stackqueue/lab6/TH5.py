class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteValue(head, x):
    if head is None:
        return None

    if head.data == x:
        return head.next

    cur = head

    while cur.next is not None:
        if cur.next.data == x:
            cur.next = cur.next.next
            return head
        cur = cur.next

    return head


def printList(head):
    cur = head
    while cur:
        print(cur.data, end=" -> ")
        cur = cur.next
    print("null")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)

print("Trước khi xóa:")
printList(head)

head = deleteValue(head, 2)

print("Sau khi xóa:")
printList(head)