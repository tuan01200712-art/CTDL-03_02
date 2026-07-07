class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def getMiddle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next


def mergeSort(head):
    if head is None or head.next is None:
        return head

    mid = getMiddle(head)
    right = mid.next
    mid.next = None

    left = mergeSort(head)
    right = mergeSort(right)

    return merge(left, right)


def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("null")


head = Node(3)
head.next = Node(1)
head.next.next = Node(2)

print("Trước khi sắp xếp:")
printList(head)

head = mergeSort(head)

print("Sau khi sắp xếp:")
printList(head)