class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeKthFromEnd(head, k):
    dummy = Node(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    for i in range(k + 1):
        if fast is None:
            return head
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


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

print("Trước khi xóa:")
printList(head)

head = removeKthFromEnd(head, 2)

print("Sau khi xóa:")
printList(head)