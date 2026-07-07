class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("null")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Trước khi đảo:")
printList(head)

head = reverse(head)

print("Sau khi đảo:")
printList(head)